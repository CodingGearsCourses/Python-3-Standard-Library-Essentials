# --------------------------------
# CodingGears.io
# --------------------------------
# Using seek

# TODO: File to work with
my_file = "sample_data/messages.txt"

# TODO: Open the file
file_handler = open(my_file, "w")

# TODO: Write to the file & use seek
file_handler.write("3: From Python Code!\n")
file_handler.seek(3)
file_handler.write("4: Magic !")

# TODO: Close the file
file_handler.close()
