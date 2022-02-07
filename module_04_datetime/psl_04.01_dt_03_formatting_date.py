# --------------------------------
# CodingGears.io
# --------------------------------
# Datetime Module

from datetime import datetime

# TODO: datetime.now
now = datetime.now()
print("Now  : {}".format(now))

# TODO: Formatting - Day of the week
print("Day of the week : " + now.strftime("%a"))
print("Day of the week : " + now.strftime("%A"))


# TODO: Formatting - Month
print("Month : " + now.strftime("%m"))
print("Month : " + now.strftime("%b"))
print("Month : " + now.strftime("%B"))


# TODO: Formatting - Day
print("Day : " + now.strftime("%d"))
print("Month : " + now.strftime("%B"))
print("Day : " + now.strftime("%A, %B %d"))

# TODO: Formatting - Year
print("Year YY    : " + now.strftime("%y"))
print("Year YYYY  : " + now.strftime("%Y"))

# TODO: Formatting - Date
print("Date : " + now.strftime("%A, %B %d, %y"))
print("Date : " + now.strftime("%A, %B %d, %Y"))
print("Date : " + now.strftime("%m-%d-%Y"))
print("Date : " + now.strftime("%m/%d/%Y"))
print("Date : " + now.strftime("%b/%d/%Y"))
