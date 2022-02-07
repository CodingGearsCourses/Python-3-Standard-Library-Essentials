# --------------------------------
# CodingGears.io
# --------------------------------
# Read file line by line

# TODO: File - data_animals.txt
file1 = "sample_data/data_animals.txt"

# TODO:  Reading using a loop
with open(file1, "r") as file_handler1:
    for line in file_handler1:
        print(line, end="")

# TODO:  Reading using "readlines"
with open(file1, "r") as file_handler2:
    lines_list = file_handler2.readlines()
    print(type(lines_list))
    print(lines_list[4])
