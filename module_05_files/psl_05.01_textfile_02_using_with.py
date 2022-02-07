# --------------------------------
# CodingGears.io
# --------------------------------
# Working with text files
# Using with

# TODO: File
my_file = "sample_data/messages.txt"

# TODO: Reading
with open(my_file, "r") as file_handler:
    file_contents = file_handler.read()
    print(type(file_contents))
print(file_contents)

# TODO: Writing
with open(my_file, "w") as file_handler:
    file_handler.write("1: From Python Code!")
    file_handler.write("\n")

# TODO: Appending
with open(my_file, "a") as file_handler:
    file_handler.write("2: From Python Code!")
    file_handler.write("\n")
