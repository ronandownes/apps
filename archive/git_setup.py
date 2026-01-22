#!/usr/bin/env python3
"""
Git Setup for E:/apps
Run this once to initialize the repo
"""
import subprocess

def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    return result.returncode

print("=== INITIALIZING GIT REPO ===\n")

# Initialize
print("Initializing git...")
run_cmd("git init")

# Set default branch to main
print("\nSetting default branch to main...")
run_cmd("git branch -M main")

# Add remote
print("\nAdding remote...")
run_cmd("git remote add origin https://github.com/ronandownes/apps.git")

print("\n✓ Git initialized and remote added")
print("\nNow run push_aggressive.py")
