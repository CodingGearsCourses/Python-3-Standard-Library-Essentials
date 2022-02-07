# --------------------------------
# CodingGears.io
# --------------------------------
# hashlib

# TODO: Imports
import hashlib

# TODO: MD5
hash_md5 = hashlib.md5()

# TODO: SHA256
hash_sha256 = hashlib.sha256()

# TODO: Determine the MD5 & SHA256 of a file
filename = "psl_08.01_hashlib_01.py"
with open(filename, "rb") as my_file:
    data = my_file.read()
    hash_md5.update(data)
    hash_sha256.update(data)
    digest_md5 = hash_md5.hexdigest()
    digest_sha256 = hash_sha256.hexdigest()

print("MD5    : {}".format(digest_md5))
print("SHA256 : {}".format(digest_sha256))

