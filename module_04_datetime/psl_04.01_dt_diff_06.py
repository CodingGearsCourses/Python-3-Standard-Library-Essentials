# --------------------------------
# CodingGears.io
# --------------------------------
# Time difference

from datetime import datetime, date

# TODO: date objects
date1 = date(2015, 12, 15)
date2 = date(2015, 11, 1)

# TODO: date object difference
d1 = date1 - date2
print("Difference     : {}".format(d1.days))
print("Object type    : {}".format(type(d1)))

# TODO: datetime objects
datetime1 = datetime(2015, 11, 18)
datetime2 = datetime(2015, 11, 1)

# TODO: datetime objects difference
d2 = datetime1 - datetime2
print("Difference     : {}".format(d2.days))
print("Object type    : {}".format(type(d2)))
