# --------------------------------
# CodingGears.io
# --------------------------------
# Read and write ZIP files

# TODO: Imports
import zipfile

# TODO: Zip file
file_name = "sample_data/my_data.zip"

# TODO: Display the contents of a zip file - M1
my_zip1 = zipfile.ZipFile(file_name, "r")
content_list = my_zip1.namelist()
# for item in content_list:
#     print(item)

# TODO: Display the contents of a zip file - M2
# with zipfile.ZipFile(file_name, "r") as my_zip2:
#     my_zip2.printdir()

# TODO: Display the zip file information
# for info in my_zip1.infolist():
#     print(info)

# TODO: Display the info of a specific file
print(my_zip1.getinfo("my_cities.txt"))

# TODO: Display the contents of a specific file (1)
print(my_zip1.read("my_cities.txt"))

# TODO: Display the contents of a specific file (2)
print("-" * 25)
with my_zip1.open("my_cities.txt") as my_file:
    print(my_file.read())
