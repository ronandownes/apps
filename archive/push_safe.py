#!/usr/bin/env python3
"""
Safe Git Push - Normal commit and push
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

print("=== NORMAL PUSH ===\n")

# Add everything
print("Adding all files...")
run_cmd("git add -A")

# Commit
print("\nCommitting...")
run_cmd('git commit -m "Update from local"')

# Normal push
print("\nPushing to remote...")
ret = run_cmd("git push origin main")

if ret == 0:
    print("\n✓ Done")
else:
    print("\n✗ Push failed - may need to pull first")
    sys.exit(1)
