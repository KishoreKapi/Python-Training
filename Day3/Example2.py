name=input()
var=input()

ct=0

for i in range(0,len(name),1):
    if(name[i]==var):
        ct=ct+1

print(ct)