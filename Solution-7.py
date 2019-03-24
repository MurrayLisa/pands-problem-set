#Solution-7 Lisa Murray

# User needs to input number that they want to calculate the square root of:
num = float(input("Please enter a positive number: "))

#square root is found by raising the number to the power of a half
sqroot = num**(1/2)

# round the square root number to one decimal place and cast as a string
ans = str(round(sqroot, 1))

#print the answer in a formatted sentence
print (f"The square root of {num} is approx. {ans}.")