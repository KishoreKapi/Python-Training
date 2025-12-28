# Given a string s consisting of words and spaces, return the length of the last word in the string.
#  012345678910
s="Hello World sidhartha college"
#s = "Hello World"
# output =5 ("World")
o=""
l=[]
for i in range(0,len(s),1): #i=11
    if(s[i]!=" "): # " " != " "
        o=o+s[i]   #o="college"
    else:
        l.append(o)
        o=""

l.append(o)
print(l)
print(l[-3])
print(l[2])
print(l[len(l)//2])
print(len(o))

