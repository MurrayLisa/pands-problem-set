
import datetime 

today = datetime.datetime.today()

dayOfMonth = int(today.strftime("%d"))

daySuf = "th"

if dayOfMonth == 3 or dayOfMonth == 23:
    daySuf = "rd"
elif dayOfMonth == 2 or dayOfMonth == 22:
    daySuf = "nd"
elif dayOfMonth == 1 or dayOfMonth == 21 or dayOfMonth == 31:
    daySuf = "st"


print(today.strftime("%A, %B %d" + daySuf + " %Y at %#I:%M %p"))




