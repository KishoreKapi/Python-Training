#Map
def square(a):
    return a**2

l=[1,2,3]
f=list(map(square,l))
print(f)

#filter
def greaterthan1(n):
    if(n>1):
        return n
    # return

f=list(filter(greaterthan1,l))
print(f)

#Lambda
f=list(filter(lambda x:x>1,l))
print(f) 

#Reduce

from functools import reduce
def multiply(a,b):
    return a*b

f=reduce(multiply,l)
print(f)

f=reduce(lambda x,y:x*y,l)
print(f)

f=lambda x,y:x if x>y else y
print(f(1,2))