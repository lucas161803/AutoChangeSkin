#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import listdir, path

# 指定要列出所有檔案的目錄
mypath = "D:/test_data"
print(mypath)
r_path = path.relpath(mypath) 
print(r_path)
# 取得所有檔案與子目錄名稱
files = listdir(r_path)

# 以迴圈處理
for f in files:
    # 產生檔案的絕對路徑
    fullpath = path.join(mypath, f)
    # 判斷 fullpath 是檔案還是目錄
    if path.isfile(fullpath):
        print("檔案：", f)
    elif path.isdir(fullpath):
        print("目錄：", f)