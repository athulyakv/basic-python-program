def dup(lst):
    dup=[]
    rst=[]
    for i in lst:
        if i not in dup:
            rst.append(i)
            dup.append(i)
    return rst
lst=[]
n=int(input('enter the limit'))
for i in range(n):
    a=int(input('enter number'))
    lst.append(a)
a=dup(lst)
print(a)
