# Programming and Scripting module at Galway-Mayo Institue of Technology
## Problem Set 2019

Completed by Lisa Murray (Student ID G00245542)

## How to download Repository
1. Go to Github and click on pands-problem-set
2. Click Clone or download
3. Ensure file type is HTTPS and click Download Zip
4. Extract file and save in desired location

## Using the Code
Make sure you have Python installed
    Open the CLI (Cmder preferable)
    Type "python" and filename e.g. $ python Solution-1.py
    Enter input as requested
    Review output


## Description

This project displays the solutions 1-10 for the Problem set 2019 issued as part of the Programming and Scripting module at Galway-Mayo Institue of Technology in semester 1 from a novice programmer.

The questions are as follows
1. Write a program that asks the user to input any positive integer and outputs the sum of all numbers between one and that number

A positive Integer is any nautral whole number. By converting the string format to number format and using loops I was able to complete this question.

2. Write a program that outputs whether or not today is a day that begins with the letter T. 

Using the datetime library, I first had to estabish the number equivlent in the weekday method i.e  Monday is 0, Tuesday is 1, Wednesday is 3 etc. Using if statements i was able to generate an output that identified if the present day was a Tuesday or Thursday

3. Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12

The range function was used here, which allows an analysis of a sequence of numbers. First the number range was checked to see if it was divisable by six by checking for a remainder, the number is only retained if no remainder existed, At the same time it checks to see if there is a remainder when diveded by 12, if a remainder exsisted the number was retained. All other number were discounted and not printed as part of the programe output.

4. Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and,if it is even,divide it by two,but if it is odd, multiply it by three and add one. Have the program end if the current value is one. 

Using if statement and while loop the above conditions were created to output the positive integer. The while loop was utilised to out put the value as long as it was not equal to zero. The If statement was used divide the number by 2 as long as the remainder was equal to zero, also if the number was 1, it was  assigned 0 so it would exit the while loop. If number was odd it was multipled by three and 1 was added

5. Write a program that asks the user to input a positive integer and tells the user whether or not the number is a prime

A prime number is a whole number greater than 1 whose only factors are 1 and itself. Using If statements and for loops, the programme checks the user inputed integer by first ensuring the number is greater than one, as we know this is not a prime. It then looped through every number from 2 to half the given number +1 and checked the modulus for each as only if the number was less than or equal to 0 after the loop, was it a prime.

6. Write a program that takes a user input string and outputs every second word. 

The sentence was split where each word which is seperated by an empty space. A temperory variable was used to track which word the loop was at so the loop would count every second word and print the result until no more words were available.


7. Write a program that takes a positive ﬂoating point number as input and outputs an approximation of its square root. 

I originally used the method of Newtons square root as per the lecture, but then researched further to identify a different method as there always seems to be multiple answers to every question. The square root is equivlent of the number to the power of a half so i used this to calculate the number and then ronded the number to 1 decimal place and printed the answer in a formatted sentence. 


8. Write a program that outputs today’s date and time in the format “Monday,January 10th 2019 at 1:15pm”. 

In time there is a 12 hour(%H) and a 24 hour(%I) clock. I had to learn how to differenciate between these so I could  esure the output of am/pm made sense. Using the datetime library, strftime and variables I was able to create the date and time in the requested format, taking into consideration that there are three suffixes to the day (th, st and rd).


9. Write a program that reads in a text ﬁle and outputs every second line. Theprogram should take the ﬁlename from an argument on the command line

Using a simialr concept to question six only differnciating between lines instead of words. I also took into consideration that the user may not necessarily but the file type into the command line (.txt) I used an if statement to add it, if it was missing from the input. 


10. Write a program that displays a plot of the functions x, x2 and 2x in the range 

Matplotlib and numpy libraries were required to help plot the graph and help format it so it could be presented as a standard graph with evenly spaced gridlines, rasonable axis lengths, with gridlines, axis titles and a legend.


## References
1. https://docs.python.org/3/tutorial/index.html
2. https://www.w3schools.com/python/
3. https://stackoverflow.com/questions/tagged/python
4. https://learnonline.gmit.ie/course/view.php?id=1588
5. https://www.pythonforbeginners.com/basics/
6. https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
7. https://swcarpentry.github.io/python-novice-gapminder/09-plotting/
