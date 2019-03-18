num = int(input ("Please insert positive Integer: "))
x=0
if num > 1:
    for i in range(2,num//2+1):
        if(num%i==0):
            x=x+1
    if(x<=0):
        print("That is a prime")
    else:
        print("That is not a prime")
else:
    print("That is not a prime")       