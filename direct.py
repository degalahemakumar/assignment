'''import os
cwd=os.getcwd()
print("cwd",cwd)

import os
os.mkdir("amon.py")


import os
cwd=os.mkdir("file1/file2/file/file4")

import os
cwd=os.mkdir("file1/hi/hello/say/nothing")

import os
os.rmdir("file1/say")

import os
os.rmdir('file1/file2/file3/file4')

import os
os.rmdir('fle1/file2/file3/file4')
print(os.listdir("abc"))

import os
os.rmdir('fle1/file2/file3/file4')
print(os.listdir("desktop"))

import os
os.rmdir('fle1/file2/file3/file4')
print(os.listdir("."))

import os
os.rename("file1","newdir")
print("file1 directory renamed to newdir")

import os
os.mkdir("new_dir")
os.mkdir("D:/new_dir")

import os
print("string format:",os.getcwd())
print("byte string format:",os.getcwdb())

import os
os.rename("file1.txt","file1_rename.txt")

import os
os.rename("file1.txt","D:/file1_rename.txt")

import os
print("current dicectory:",os.getcwd())
os.chdir('/hema/kumar/prakash/desktop/')
print("current directory:",os.getcwd)

import os
print("files in CWD are:",os.listdir(os.getcwd()))

import os
dir_li=os.listdir("K:/files")
if len(dir_li)==0:
    print("errors!!directory are not empty!!")
else:
    os.rmdir("K:/files")'''

import os
cwd='/'
print(os.path.isdir(cwd))
other='k:/'
print(os.path.isdir(other))   

import os
print(os.path.getsize(os.getcwd()))

import os
import datetime as dt
print("before conversion:")
print("last access time:",os.path.getatime(os.getcwd()))
print("last modification time:",os.path.getmtime(os.getcwd()))
print("after conversion:")
access_time=dt.datetime.fromtimestamp(os.path.getatime(os.getcwd())).strftime("%Y-%m-%d %I:%M %p")
modification_time=dt.datetime.fromtimestamp(os.path.getmtime(os.getcwd())).strftime("%Y-%m-%d %I:%M %p")
print("last access time:",access_time)
print("last modification time:",modification_time)

import filecmp as fc
import os
dir_1=dir_2=os.getcwd()
d=fc.dircmp(dir_1, dir_2, ignore=none, hide=none)
print("comparsion 1:")
d.report()