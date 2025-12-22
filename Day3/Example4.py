name=input()
i=0
output=""
while(i<len(name)):
    if(name[i]=="a" or name[i]=="e" or name[i]=="i" or name[i]=="o" or name[i]=="u"):
        output=output+name[i]
    i=i+1
print(output)
