# Solution-1 
# User needs to enter integer
number = input("Please enter a positive integer:")
# Number needs to be converted from string format to number format, and add 1 to inclued the number chosen
num2 = int(number) + 1
# Creating variable for sum
sum = 0
# create loop to loop through all numbers up to number user entered
for i in range(num2):
    sum += i
# Print the sum to the screen
print (sum)
