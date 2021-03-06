#Program to illustrate Python Directory and Files Management

import os


x=os.getcwd()#get the present working directory using the getcwd() method.
print(x)

os.chdir('D:\\')#change the current working directory using the chdir() method.
print(os.getcwd())

print(os.listdir('d:\\'))
""""This method takes in a path and returns a list of sub directories and files in that path. 
If no path is specified, it returns from the current working directory.
"""

os.mkdir('samples')#make a new directory using the mkdir() method.
print(os.listdir('d:\\Test'))

os.rename('d:\\sample','new_one')#rename() method can rename a directory or a file.


os.remove('t.py')
os.rmdir('d:\\new_one')
""""
File can be removed (deleted) using the remove() method.
rmdir() method can only remove empty directories.
"""

""" shutil in Python is a module that offers several functions to deal with operations on files and their collections. It provides the ability to copy and removal of files."""
import shutil

shutil.rmtree('new_one')

""""
to remove a non-empty directory we can use the rmtree() method 
which belongs from shutil module.
"""

print(shutil.which("python"))

# which() to show the directory of an exe

shutil.copy('mv.txt','d:\\')
#  copy a file from one location to another using copy().

shutil.move('mv.txt','d:\\')
# move a file from one location to another using move().

shutil.disk_usage('c:\\')
