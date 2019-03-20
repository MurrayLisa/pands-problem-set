word = input ("Please enter a sentence: ")
words = word.split(' ')
count = 0
for x in words:
    if count <len(words):
        print (words[count])
        count += 2
        