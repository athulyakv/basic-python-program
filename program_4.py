'''write a program to print the no. of vowels in a given txt'''
a=(input('enter text:'))
c=0
for i in a:
    if i in 'AEIOUaeiou':
        c+=1
print(c)
