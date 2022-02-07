# --------------------------------
# CodingGears.io
# --------------------------------
# timeit Module
# This module provides a simple way to time small bits of Python code.

import random
import time
from timeit import default_timer as timer


# TODO: Simple sleep function
def magic():
    counter = random.randint(1, 10)
    print("I am sleeping for {} seconds!".format(counter - 1))
    for i in range(1, counter):
        print(i, end=" ")
        time.sleep(1)


# TODO: Start the timer
start_time = timer()

# TODO: Call magic function
magic()

# TODO: after the execution
print()
end_time = timer()
print("Time Difference : {}".format(end_time - start_time))

