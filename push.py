# push_to_github.py
# Purpose: add + commit + (optional pull --rebase) + push a repo to GitHub from Windows.
# Put this file in the ROOT of your repo (e.g. E:\apps\push_to_github.py) and run it.

from __future__ import annotations

import argparse
import datetime as dt
import os
import shutil
import subprocess
import sys
from pathlib import Path


def run(cmd: list[str], cwd: Path, check: bool = True) -> subprocess.CompletedProcess:
    # Use text mode so stdout/stderr are readable
    return subprocess.run(cmd, cwd=str(cwd), text=True, capture_output=True, check=check)


def require_git() -> None:
    if shutil.which("git") is None:
        print("ERROR: 'git' not found on PATH. Install Git for Windows first.")
        sys.exit(1)


def is_git_repo(repo: Path) -> bool:
    try:
        run(["git", "rev-parse", "--is-inside-work-tree"], cwd=repo)
        return True
    except subprocess.CalledProcessError:
        return False


def current_branch(repo: Path) -> str:
    cp = run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=repo)
    return cp.stdout.strip()


def has_changes(repo: Path) -> bool:
    cp = run(["git", "status", "--porcelain"], cwd=repo)
    return bool(cp.stdout.strip())


def main() -> int:
    parser = argparse.ArgumentParser(description="Commit and push a Git repo to GitHub.")
    parser.add_argument(
        "--repo",
        type=str,
        default=".",
        help="Path to repo (default: current folder). Example: E:\\apps",
    )
    parser.add_argument("--remote", type=str, default="origin", help="Remote name (default: origin)")
    parser.add_argument("--branch", type=str, default="", help="Branch to push (default: current branch)")
    parser.add_argument("--message", type=str, default="", help="Commit message (default: timestamped)")
    parser.add_argument(
        "--pull-rebase",
        action="store_true",
        help="Do 'git pull --rebase' before pushing (recommended if you edit from multiple machines).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would happen without changing anything.",
    )
    args = parser.parse_args()

    require_git()

    repo = Path(args.repo).expanduser().resolve()
    if not repo.exists():
        print(f"ERROR: Repo path does not exist: {repo}")
        return 1

    if not is_git_repo(repo):
        print(f"ERROR: Not a git repository: {repo}")
        print("If this is meant to be a repo, run: git init (and set a remote).")
        return 1

    branch = args.branch.strip() or current_branch(repo)
    remote = args.remote.strip()

    # Quick info
    print(f"Repo:   {repo}")
    print(f"Remote: {remote}")
    print(f"Branch: {branch}")

    # Show status
    cp = run(["git", "status"], cwd=repo, check=True)
    print(cp.stdout.rstrip())

    if not has_changes(repo):
        print("Nothing to commit. Pushing anyway (in case commits exist locally).")
    else:
        msg = args.message.strip()
        if not msg:
            stamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            msg = f"Update {stamp}"

        print(f"Commit message: {msg}")

        if args.dry_run:
            print("DRY RUN: would run: git add -A")
            print(f"DRY RUN: would run: git commit -m {msg!r}")
        else:
            run(["git", "add", "-A"], cwd=repo, check=True)
            # Commit might fail if only whitespace changes etc; handle gracefully
            try:
                run(["git", "commit", "-m", msg], cwd=repo, check=True)
            except subprocess.CalledProcessError as e:
                # If nothing staged (rare edge case), show output and continue to push
                print("NOTE: Commit did not complete. Output:")
                print((e.stdout or "").rstrip())
                print((e.stderr or "").rstrip())

    if args.pull_rebase:
        if args.dry_run:
            print(f"DRY RUN: would run: git pull --rebase {remote} {branch}")
        else:
            try:
                run(["git", "pull", "--rebase", remote, branch], cwd=repo, check=True)
            except subprocess.CalledProcessError as e:
                print("ERROR: Pull --rebase failed. Fix conflicts, then rerun.")
                print((e.stdout or "").rstrip())
                print((e.stderr or "").rstrip())
                return 1

    if args.dry_run:
        print(f"DRY RUN: would run: git push {remote} {branch}")
        return 0

    try:
        run(["git", "push", remote, branch], cwd=repo, check=True)
        print("Push complete.")
        return 0
    except subprocess.CalledProcessError as e:
        print("ERROR: Push failed.")
        print((e.stdout or "").rstrip())
        print((e.stderr or "").rstrip())
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
