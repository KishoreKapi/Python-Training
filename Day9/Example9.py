l=[0,1,1,2,2,3,4,4,2]
#  0 1 2 3 4 5 6 7 8

#output=[0,1,2,3,4]

output=[]

output_single_values=[]

d={}
#d={1:"hi"}
#d.get(1)=d[1]="hi"

#d={}
#d.get(1)=None
#d[1]=error
for i in range(0,len(l),1): #i=0,1,2,3,4,5,6,7,8
    if(d.get(l[i])==None): # 2=="None"
        d[l[i]]=1 # d={0:1,1:2,2:3,3:1,4:2}
    else:
        d[l[i]]=d[l[i]]+1 #d[2]=3
    
print(d)
for i,j in d.items():
    output.append(i)

print(output)

for i,j in d.items():
    if(j==1):
        output_single_values.append(i)

print(output_single_values)

