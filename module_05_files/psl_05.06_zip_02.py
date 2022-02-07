# --------------------------------
# CodingGears.io
# --------------------------------
# Read and write ZIP files

# TODO: Imports
import zipfile

# TODO: Zip file
file_name = "sample_data/my_data.zip"

# TODO: Reading zip file
my_zip = zipfile.ZipFile(file_name, 'r')

# TODO: Extract one file
# my_zip.extract("my_animals.txt")

# TODO: Extract everything
# my_zip.extractall()

# TODO: Extract to a folder
my_zip.extractall("my_folder1")