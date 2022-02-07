# --------------------------------
# CodingGears.io
# --------------------------------
# statistics Module
# This module provides functions for calculating mathematical
# statistics of numeric (Real-valued) data.

import statistics as stat

numbers = [10, 23, 49, 45, 89, 23, 21, 89, 99]

# TODO: Mean, Mode, Median
result_mean = stat.mean(numbers)
print("The average is {}".format(round(result_mean, 3)))

result_mode = stat.mode(numbers)
print("The mode is {}".format(result_mode))

result_median = stat.median(numbers)
print("The median is {}".format(result_median))

# TODO: Variance, Std. Deviation
result_var = stat.variance(numbers)
print("The variance is {}".format(result_var))

result_std = stat.stdev(numbers)
print("The std. dev is {}".format(result_std))

