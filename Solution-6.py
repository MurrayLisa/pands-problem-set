#Solution-6 Lisa Murray


# User needs to enter sentence
word = input ("Please enter a sentence: ")

#splits the sentence into each word which is seperated by an empty space
words = word.split(' ')

#initiate temperory variable to 0 to track which word the loop is at
count = 0

#loop through every word in the words array
for x in words:

    #if we have not reached the end of the array print the current word and add two to the count variable so that we will skip the next word.
    if count <len(words):
        print (words[count], end=' ')
        count += 2
        