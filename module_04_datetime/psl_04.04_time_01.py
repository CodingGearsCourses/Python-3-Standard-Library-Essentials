# --------------------------------
# CodingGears.io
# --------------------------------
# time Module

import time
import random

# TODO: Epoch Time
print(time.time())

# TODO: Using sleep
counter = random.randint(1, 5)
print("Counter Value : {}".format(counter))
print("Sleeping for {} second(s)".format(counter - 1))

for i in range(1, counter):
    print(i, end=" ")
    time.sleep(1)


