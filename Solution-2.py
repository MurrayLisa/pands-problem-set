# Solution-2 - Lisa Murray

#Import Library
import datetime

#Assigning todays date and time from datetime to variable day
day = datetime.datetime.today().weekday()

# Tuesday is day 1 and thursday is day 3 in the weekday method in the datetime library
if day == 1 or day == 3:
    print ("Yes - today begins with a T")
else:
    print ("No Today does not begin with a T")