# --------------------------------
# CodingGears.io
# --------------------------------
# Datetime Module
# Time Delta

from datetime import datetime, timedelta

# TODO: datetime.now
now = datetime.now()

# TODO: Future
future_date = now + timedelta(weeks=1, days=2)
print("future_date : {}".format(future_date.date()))

# TODO: Past
past_date = now - timedelta(days=2)
print("past_date : {}".format(past_date.date()))

# TODO: Compare
dt1_now = datetime.now()
dt2_future = dt1_now + timedelta(days=2)
dt3_past = dt1_now - timedelta(days=2)

if dt1_now > dt2_future:
    print("A: dt1_now : {}".format(dt1_now))
else:
    print("A: dt2_future : {}".format(dt2_future))

if dt1_now > dt3_past:
    print("B: dt1_now : {}".format(dt1_now))
else:
    print("B: dt3_past : {}".format(dt3_past))
