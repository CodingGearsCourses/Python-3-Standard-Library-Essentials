# --------------------------------
# CodingGears.io
# --------------------------------
# Working with text files
# Using open

# TODO: File
myfile = "sample_data/messages.txt"

# TODO: Write to file
writer = open(myfile, "w")
writer.write("line1\n")
writer.write("line2\n")

# TODO: Close the file
writer.close()


