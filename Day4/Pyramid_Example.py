n=input("Enter Number\n")
n=int(n)
a=n
for i in range(1,n+1,1):
    print(" "*a+" *"*i)
    a=a-1