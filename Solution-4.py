# Solution -4
num = input ("Please insert positive Integer: ")
intnum = int(num)
while intnum != 1:
    print (intnum)
    if intnum % 2 == 0:
        intnum = int(intnum / 2)
    else:
        intnum = (intnum * 3) + 1