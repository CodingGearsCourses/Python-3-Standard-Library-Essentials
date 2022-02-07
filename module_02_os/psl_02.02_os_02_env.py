# CodingGears.io
# Environment Variables

import os


# TODO: Access Environment Variables
print(os.environ['HOME'])

# TODO: Check specific environment variable
if 'USERS' in os.environ:
    print("Found!")
else:
    print("Not Found!")

# TODO: Read all environment variables
for item, value in os.environ.items():
    print("{} -- {}".format(item, value))

# TODO: Invalid Env variable
print(os.environ['HOME2'])
