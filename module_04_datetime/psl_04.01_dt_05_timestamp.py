# --------------------------------
# CodingGears.io
# --------------------------------
# Timestamp (Epoch Unix Timestamp)
# Seconds since Jan 01 1970 (UTC)

from datetime import datetime

# TODO: datetime.now
now = datetime.now()
print("Now : " + str(now))

# TODO: Displaying timestamp (Converting datetime to timestamp)
print("Timestamp : {}".format(now.timestamp()))

# TODO: Displaying timestamp (Converting timestamp to datetime)
timestamp1 = 1543865929
dt = datetime.fromtimestamp(timestamp1)
print("dt   : {}".format(dt))
print("Type : {}".format(type(dt)))

