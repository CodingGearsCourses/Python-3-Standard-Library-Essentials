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
from math import sqrt
'''

stmt_code = '''
sum = 0
for x in range(1, 10000):
    sum += sqrt(x)
'''

iterations = 10000

duration = timeit.timeit(stmt=stmt_code, setup=setup_code, number=iterations)

print(duration)
