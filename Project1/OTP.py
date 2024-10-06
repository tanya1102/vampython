#Create a python program to generate random 6 digit otp.

from random import randint 

for i in range(6):
    print(randint(0,9),end='')

#NOTES:-

#random variable generators used to pick random element or random sample.
#import used to load the namespace of what is available in that python module, into memory.
#randint function used to generate random integers between two specified values.
#range returns an object that produces a sequence of integers from start.
#passing whitespace to the end parameter (end=' ') indicates that end character has to be identified by whitespace and not a newline.