# CodingGears.io
# Using glob
# Unix style pathname pattern expansion

import glob

# TODO: Using *
location = "sample_data/data1/*"

for name in glob.glob(location):
    print(name)

# TODO: Using ?
location = "sample_data/data1/bost*-0?.txt"

for name in glob.glob(location):
    print(name)

# TODO: Using Range
location = "sample_data/data1/bost*-0[1-5].txt"

for name in glob.glob(location):
    print(name)

# TODO: Using Recursive
location = "sample_data/**/*bird*-0[1-5].gif"

for name in glob.glob(location, recursive=True):
    print(name)