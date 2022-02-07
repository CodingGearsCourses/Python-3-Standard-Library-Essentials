# --------------------------------
# CodingGears.io
# --------------------------------
# The pickle module implements binary protocols for serializing
# and de-serializing a Python object structure.

import pickle

phone_number_list = [["John", "111-111-1111"],
                     ["Peter", "222-222-222"],
                     ["Mouse", "333-333-3333"]]

# TODO: File
my_file = "sample_data/phone.bin"

# TODO: Write to binary file
with open(my_file, "wb") as file_handler1:
    pickle.dump(phone_number_list, file_handler1)

# TODO: Read from binary file
with open(my_file, "rb") as file_handler2:
    phone_list = pickle.load(file_handler2)
    print(type(phone_list))
    print(phone_list)
