#!/usr/bin/env python3
import subprocess

print("Force pushing all changes...")
subprocess.run(['git', 'add', '-A'], shell=True)
subprocess.run(['git', 'commit', '-m', 'Force update'], shell=True)
subprocess.run(['git', 'push', '--force'], shell=True)
print("Done!")