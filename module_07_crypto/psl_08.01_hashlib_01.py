# --------------------------------
# CodingGears.io
# --------------------------------
# hashlib

# TODO: Imports
import hashlib

data = "CodingGears.io"

# TODO: MD5
hash_md5 = hashlib.md5()
hash_md5.update(data.encode("utf-8"))
digest = hash_md5.hexdigest()
print("MD5    : {}".format(digest))

# TODO: SHA1
hash_sha1 = hashlib.sha1()
hash_sha1.update(data.encode("utf-8"))
digest = hash_sha1.hexdigest()
print("SHA1   : {}".format(digest))

# TODO: SHA256
hash_sha256 = hashlib.sha256()
hash_sha256.update(data.encode("utf-8"))
digest = hash_sha256.hexdigest()
print("SHA256 : {}".format(digest))

# TODO: SHA512
hash_sha512 = hashlib.sha512()
hash_sha512.update(data.encode("utf-8"))
digest = hash_sha512.hexdigest()
print("SHA512 : {}".format(digest))
