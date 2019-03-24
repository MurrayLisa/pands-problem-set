
import datetime 

today = datetime.datetime.today()

dayOfMonth = int(today.strftime("%d"))
hour = int(today.strftime("%H"))

daySuf = "th"
timeSuf = "pm"
if dayOfMonth == 3 or dayOfMonth == 23:
    daySuf = "rd"
elif dayOfMonth == 2 or dayOfMonth == 22:
    daySuf = "nd"
elif dayOfMonth == 1 or dayOfMonth == 21 or dayOfMonth == 31:
    daySuf = "st"

if hour < 13:
    timeSuf = "am"


print(today.strftime("%A, %B %d" + daySuf + " %Y at %H:%M" + timeSuf))




