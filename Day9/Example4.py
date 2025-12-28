# l=[1,2,3] #len(l)=3
l=[4,3,2,1]
#output=[1,2,4] 123+1=124 --> [1,2,4]
output=[]
s=""
for i in range(0,len(l),1): #i=3
    s=s+str(l[i])   # "12" + "3" ="123" String concatination
s=int(s) + 1 # "123" --> 123 + 1 = 124
s=str(s) # 124 --> "124"
for i in range(0,len(s),1): # 1=0 --> 2
    output.append(int(s[i])) # [] "1" --> 1 --> [1,2,4]
    
print(output)
