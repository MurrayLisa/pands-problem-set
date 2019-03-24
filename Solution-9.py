#Solution-9 Lisa Murray

#User to input file name
filepath = input ("Please enter a file name: ")

#if the user does not input the file format(ie .txt),add the file format to file name 
if ".txt" not in filepath:
    filepath = filepath + ".txt"

# open the user file using the with keyword to wrap the code so that the file does not have to be closed afterwards
with open(filepath) as f:


#initialise temporary variable with 1 to start at the first line
    count = 1
    
    #loop through every line in the file and if the modulus of the line count is zero print the line
    for line in f:
        count+=1
        if count % 2 == 0: 
            print(line)
        