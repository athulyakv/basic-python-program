'''write a prgm to shuffle and print a specified list'''
from random import shuffle

def shuffle_Color(c):
    shuffle(c)
    return c

c=['red', 'orange', 'white'] 

b = shuffle_Color(c)
print(b)
