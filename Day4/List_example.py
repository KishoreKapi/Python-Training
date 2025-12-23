l=[1,3,2,2,4,7,3]
a=[]
for i in range(0,len(l),1):
    if(l[i] not in a):
        a.append(l[i])
        cnt=0
        for j in range(0,len(l),1):
            if(l[i]==l[j]):
                cnt=cnt+1
        print(l[i],cnt)