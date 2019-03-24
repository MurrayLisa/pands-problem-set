# Solution-4 Lisa Murray

# User needs to enter integer
num = int (input("Please insert positive Integer: "))

# While number is not equal to zero print the number in one line
while num != 0:
    print (num, end=' ')

#If the numbers remainder is zero, divide the number by 2, also if the number is 1 assign 0 to num thus exiting the while loop. 
    if num % 2 == 0:
        num = int(num / 2)
    elif num ==1:
        num = 0

#Or if number is odd multiple by three and add 1
    else:
        num = (num * 3) + 1