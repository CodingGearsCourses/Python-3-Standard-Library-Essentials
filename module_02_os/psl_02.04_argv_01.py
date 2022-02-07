# CodingGears.io
# argv

import sys


# TODO: Command line arguments
count = len(sys.argv) - 1
print("Total : {}".format(count))

# TODO: Script Name
print("Script Name : {}".format(sys.argv[1]))

# TODO: Print all arguments - 1
# i = 0
# for a in sys.argv:
#     print(sys.argv[i])
#     i += 1

# TODO: Print all arguments - 2
print("Arguments Passed:", end=" ")
total_args = len(sys.argv)
for arg in range(1, total_args):
    print(sys.argv[arg], end=" ")
print()
