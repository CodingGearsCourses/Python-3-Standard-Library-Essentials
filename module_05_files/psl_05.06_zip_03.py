# --------------------------------
# CodingGears.io
# --------------------------------
# Read and write ZIP files

# TODO: Imports
import zipfile
import os

# TODO: Zip file name
zip_file_name = "./backup_zips/my_backup_files.zip"

# TODO: Folder to zip
my_folder = "./sample_data_2"

# TODO: Get all file paths recursively
my_file_paths = []
for root, dirs, files in os.walk(my_folder):
    for file in files:
        file_path = os.path.join(root, file)
        my_file_paths.append(file_path)

# TODO: List of files to be zipped
print("-" * 25)
for file_name in my_file_paths:
    print(file_name)

# TODO: Add files to the zip file
with zipfile.ZipFile(zip_file_name, "w") as z_file:
    for file_name in my_file_paths:
        z_file.write(file_name)

