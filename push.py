#!/usr/bin/env python3
import subprocess
import sys
import os

def push_apps():
    print("=" * 60)
    print("Git Push for ronandownes")
    print(f"Email: ronandownes@gmail.com")
    print(f"Repo: {os.getcwd()}")
    print("=" * 60)
    
    # Show current status
    print("\n📊 Current Git Status:")
    status = subprocess.run(['git', 'status'], 
                          capture_output=True, text=True, shell=True)
    print(status.stdout[:500])  # First 500 chars
    
    # Add all changes (including deletions)
    print("\n1️⃣ Adding all changes...")
    add_result = subprocess.run(['git', 'add', '-A'], 
                              capture_output=True, text=True, shell=True)
    if add_result.stdout:
        print(f"   {add_result.stdout.strip()}")
    
    # Commit
    print("\n2️⃣ Committing changes...")
    commit_result = subprocess.run(['git', 'commit', '-m', 'Update apps - ronandownes'], 
                                 capture_output=True, text=True, shell=True)
    if commit_result.stdout:
        print(f"   {commit_result.stdout.strip()}")
    if "nothing to commit" in commit_result.stderr:
        print("   ℹ️ No changes to commit")
    
    # Push
    print("\n3️⃣ Pushing to remote...")
    push_result = subprocess.run(['git', 'push'], 
                               capture_output=True, text=True, shell=True)
    if push_result.stdout:
        print(f"   {push_result.stdout.strip()}")
    if push_result.stderr:
        if "fatal" in push_result.stderr:
            print("   ❌ Push failed")
            print(f"   Error: {push_result.stderr.strip()}")
        else:
            print(f"   {push_result.stderr.strip()}")
    
    # Show final status
    print("\n" + "-" * 50)
    print("Final Status:")
    subprocess.run(['git', 'status', '--short'], shell=True)
    
    print("\n" + "=" * 60)
    print("✅ Push completed!")
    
    # Show remote info if available
    remote_result = subprocess.run(['git', 'remote', '-v'], 
                                 capture_output=True, text=True, shell=True)
    if remote_result.stdout:
        print("\n📡 Remote repositories:")
        print(remote_result.stdout.strip())

if __name__ == "__main__":
    push_apps()