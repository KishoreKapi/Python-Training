name=input()
# var=input()

# ct=0
for i in range(0,len(name),1):
    ct=0
    var=name[i]
    for j in range(0,len(name),1):
        if(name[j]==var):
            ct=ct+1
    print(name[i],ct)