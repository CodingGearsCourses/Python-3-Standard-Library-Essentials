# --------------------------------
# CodingGears.io
# --------------------------------
# tempfile — Generate temporary files and directories

# TODO: Imports
import os
import tempfile

# TODO: Create a temporary directory
temp_dir1 = tempfile.TemporaryDirectory("_sample1")

# TODO: Display temporary directory information
print("Dir created     : {}".format(temp_dir1.name))
print("Type            : {}".format(type(temp_dir1)))

# TODO: Using temporary directory
path = os.path.join(temp_dir1.name, "my_temp_file.txt")
print("File Path       : {}".format(path))
tmp_file = open(path, "w+t")
tmp_file.write("1: Writing to the temp file inside the temp dir!\n")
tmp_file.write("2: Writing to the temp file inside the temp dir!\n")
tmp_file.write("3: Writing to the temp file inside the temp dir!\n")
tmp_file.seek(0)
print(tmp_file.read())
var = input("Please check the file system....")