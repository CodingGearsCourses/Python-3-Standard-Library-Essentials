# --------------------------------
# CodingGears.io
# --------------------------------
# tempfile — Generate temporary files and directories

# TODO: Imports
import tempfile

# TODO: Create a temporary file
temp_file = tempfile.NamedTemporaryFile()

# TODO: Display temp file info
print("File created     : {}".format(temp_file))
print("Type             : {}".format(type(temp_file)))
print("Name of the file : {}".format(temp_file.name))


# TODO: Write
temp_file.write(b"1: Writing to the temp file...\n")
temp_file.write(b"2: Writing to the temp file...")

# TODO: Read
temp_file.seek(0)
print(temp_file.read())

# TODO:: Pause
var = input("Go check the file system...?..")

# TODO: Close
temp_file.close()

