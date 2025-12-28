# s="([{}])"
#  012345
s="(){}[]"

l=[]
for i in range(0,len(s),1): # (0,6,1) i=4
    if(len(l)==0):
        l.append(s[i]) # l=[]
    else:
        #     (1       and     1 )=1  or     (0       and    0 )=0  or   ( 0       and   0) = 0-->1
        if((l[-1]=="{" and s[i]=="}") or (l[-1]=="[" and s[i]=="]") or (l[-1]=="(" and s[i]==")")):
            l.pop()
        else:
            l.append(s[i])
            
print(l)
if(len(l)==0):
    print("True")
else:
    print("False")