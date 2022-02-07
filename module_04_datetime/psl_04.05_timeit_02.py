# --------------------------------
# CodingGears.io
# --------------------------------
# timeit Module
# timeit.timeit(stmt, setup, timer, number)
# stmt: The code snippet whose execution times is to be measured.
# setup: The code to run before executing stmt.
# timer: It is a default timeit.Timer object.
# number: It specifies the number of times stmt will be executed.

import timeit

setup_code = '''
import time
import random
'''

stmt_code = '''
counter = random.randint(1, 10)
print()
print("I am sleeping for {} seconds!".format(counter - 1))
for i in range(1, counter):
    print(i, end=" ")
    time.sleep(1)
print()
print("-" * 25)
'''

iterations = 5

duration = timeit.timeit(stmt=stmt_code, setup=setup_code, number=iterations)
print()
print("Duration : {}".format(duration))
