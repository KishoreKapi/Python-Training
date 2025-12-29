l=[0,1,2,2,3,0,4,2]
#                ^
val=0
#output=5
count=0

for i in range(0,len(l),1): #i=0,1,2,3,4,5,6,7
    if(l[i]!=val): # 2!=2
        print(l[i])
        count=count+1 #count=0+1+1+1+1+1=5

print("Count is",count)