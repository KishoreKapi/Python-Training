cnt=0 # global variable
def apple():
    global cnt
    cnt=cnt+1
    print("Hello Apple")
    if(cnt!=20):   # base condition
        apple()

apple()

# we have local and global variables in python.
# Local variables are inside functions or methods.
# global variables are outside functions or methods.