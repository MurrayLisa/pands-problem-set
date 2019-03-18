# Solution to Problem 2

import datetime
day = datetime.datetime.today().weekday()
if day == 1 or day == 3:
    print ("Yes - today begins with a T")
else:
    print ("No Today does not begin with a T")