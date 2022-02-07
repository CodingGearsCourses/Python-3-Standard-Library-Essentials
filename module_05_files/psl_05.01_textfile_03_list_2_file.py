# --------------------------------
# CodingGears.io
# --------------------------------
# Writing list items to a file

# Sample List
animals = ['dog', 'cat', 'hen', 'fox', 'elephant', 'snake', 'pig']

# TODO: File
file1 = "sample_data/animals.txt"

# TODO: Write to file
with open(file1, "w") as file_handler:
    for animal in animals:
        file_handler.write(animal + "\n")
