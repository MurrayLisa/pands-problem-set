#Solution-5 Lisa Murray

# User needs to enter integer
num = int(input ("Please insert positive Integer: "))

#initiate temperory variable to 0
x=0

#check first if the given number was 1 because if so we know its not a prime
if num > 1:

    #loop through every number from 2 to half the given number +1 and check the modulus for each
    for i in range(2,num//2+1):
        if(num%i==0):
            x=x+1

    # only if x is less than or equal to 0 after loop, then it is prime        
    if(x<=0):
        print("That is a prime")
    else:
        print("That is not a prime")

# if number is less than one, skips loop as it is not a prime        
else:
    print("That is not a prime")       