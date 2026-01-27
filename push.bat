@echo off
cd /d E:\apps
C:\Users\user\AppData\Local\Programs\Python\Python311\python.exe app-index-builder.py
git add .
git commit -m "Update apps"
git push
pause