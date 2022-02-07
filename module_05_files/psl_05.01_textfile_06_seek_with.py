# --------------------------------
# CodingGears.io
# --------------------------------
# Using seek

# TODO: File to work with
my_file = "sample_data/cities.txt"

# TODO: Writing (a+ = read after writing)
with open(my_file, "a+") as file_handler:
    file_handler.write("New York\n")
    file_handler.write("Boston\n")
    file_handler.write("Paris\n")
    file_handler.write("San Jose\n")
    file_handler.seek(0)
    data = file_handler.read()
    print(data)
