#Solution-8 Lisa Murray

#Import todays date and time from library and saved to a variable
import datetime 
today = datetime.datetime.today()

#single out the day attribute and save as an integer to a variable
dayOfMonth = int(today.strftime("%d"))

#temportary variable for the suffix at the end of the day eg. 3rd, initialise with most common 'th'
daySuf = "th"

#check if the day of the month needs to be changed from 'th' to a different suffix and if so assign this to daySuf
if dayOfMonth == 3 or dayOfMonth == 23:
    daySuf = "rd"
elif dayOfMonth == 2 or dayOfMonth == 22:
    daySuf = "nd"
elif dayOfMonth == 1 or dayOfMonth == 21 or dayOfMonth == 31:
    daySuf = "st"

#print the date and time in a specific format using strftime directives and my suffix variable
print(today.strftime("%A, %B %d" + daySuf + " %Y at %#I:%M %p"))




