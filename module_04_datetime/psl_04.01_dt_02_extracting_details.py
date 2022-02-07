# --------------------------------
# CodingGears.io
# --------------------------------
# Datetime Module

from datetime import datetime

# TODO: datetime.now
dt_object = datetime.now()
print("Type  : {}".format(type(dt_object)))
print("Type  : {}".format(str(dt_object)))

# TODO: Extracting date, month, year
print("Date     : {}".format(dt_object.date()))
print("Month    : {}".format(dt_object.month))
print("Year     : {}".format(dt_object.year))

# TODO: Extracting day, hour, minute, second
print("Day          : {}".format(dt_object.day))
print("Hour         : {}".format(dt_object.hour))
print("Minute       : {}".format(dt_object.minute))
print("Second       : {}".format(dt_object.second))


# TODO: time
print("Time : {}".format(dt_object.time()))
