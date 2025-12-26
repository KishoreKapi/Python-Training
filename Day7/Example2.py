# 0,1,1,2,3,5,8,13,21,34,55.... Fibonocci series
# 0,1,2,3,4,5,6,7, 8, 9, 10.... Index

# Need to find 50th index
n=5
def fib(n):
    if(n==1 or n==0):  # base condition
        return n
    return fib(n-1)+fib(n-2)

print(fib(n))

# fib(5) = fib(4)+fib(3)
# fib(4) + fib(3)
# fib(3)+fib(2)+fib(2)+fib(1)
# fib(2)+fib(1)+fib(1)+fib(0)+fib(1)+fib(0)+1
# fib(1)+fib(0)+1+1+0+1+0+1
# 1+0+1+1+0+1+0+1
# 5

# 50 #1 1
# 49,48 #2 1*2
# 48,47,47,46 #4 2*2
# 47,46,46,45,46,45,45,44 #8 4*2
