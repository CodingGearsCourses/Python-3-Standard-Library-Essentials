# --------------------------------
# CodingGears.io
# --------------------------------
# Datetime Module

from datetime import datetime

# TODO: datetime.now
now = datetime.now()
print("Now  : {}".format(now))

# TODO: Extracting hours, minutes and seconds
print("Hours    : " + str(now.strftime("%H")))
print("Minutes  : " + str(now.strftime("%M")))
print("Seconds  : " + str(now.strftime("%S")))
print("AM/PM    : " + str(now.strftime("%p")))


# TODO: Displaying time in desired format
print("Time : " + str(now.strftime("%H:%M:%S %p")))

