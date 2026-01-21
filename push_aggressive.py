#!/usr/bin/env python3
"""
Aggressive Git Push - Forces local state to remote
Run from: E:/apps
"""
import subprocess
import sys

def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    return result.returncode

print("=== AGGRESSIVE PUSH - LOCAL OVERWRITES REMOTE ===\n")

# Add everything
print("Adding all files...")
run_cmd("git add -A")

# Commit
print("\nCommitting...")
run_cmd('git commit -m "Sync from local"')

# Force push
print("\nForce pushing to remote...")
ret = run_cmd("git push --force origin main")

if ret == 0:
    print("\n✓ Done - local state forced to remote")
else:
    print("\n✗ Push failed - check errors above")
    sys.exit(1)
