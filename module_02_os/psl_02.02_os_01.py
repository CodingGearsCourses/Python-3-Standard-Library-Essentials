# CodingGears.io
import os
import sys


# TODO: Get the current working directory (CWD) - os.getcwd
location = os.getcwd()
print(location)

# TODO: Change the directory - os.chdir
os.chdir('/home/training')
print(os.getcwd())

# TODO: Create Directories - os.mkdir
location = "/home/training"
dir_name ="hello1"
# /home/training/hello1
full_path = os.path.join(location, dir_name)
if os.path.exists(full_path):
    print("Path {} already exists!".format(full_path))
    sys.exit()
os.mkdir(full_path)

# TODO: check if it is a directory or a file - os.path.isdir & os.path.isfile
location = "/home/training"
dir_name = "hello3"
# /home/training/hello1
full_path = os.path.join(location, dir_name)

if os.path.isdir(full_path):
    print("Path {} is a directory!".format(full_path))
if os.path.isfile(full_path):
    print("Path {} is a file!".format(full_path))


# TODO: List - os.listdir
location = "/home/training"

dir_list = os.listdir(location)

for item in dir_list:
    print(item)

