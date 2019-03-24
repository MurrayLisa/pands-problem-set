

filepath = input ("Please enter a file name: ")
if ".txt" not in filepath:
    filepath = filepath + ".txt"

with open(filepath) as f:

    count = 1
    for line in f:
        count+=1
        if count % 2 == 0: #this is the remainder operator
            print(line)
        