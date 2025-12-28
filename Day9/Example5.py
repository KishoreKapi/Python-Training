# [1,3,5,6] target=2
# [1,2,3,5,6] 
#  0 1 2 4 5 output = 1
# l=[1,3,5,6]
#  0 1 2 3 4
l=[2,4,7,9,10]
target=8
i=0
#range(0,len(l),1)
output=[]
while(i<len(l)): # i=3
    if(target<=l[i]): # 8<9
        output.append(target) # [2,4,7,8]
        break
    else:
        output.append(l[i]) # [2,4,7]
    i=i+1
output=output+l[i:] # [2,4,7,8] + [9,10] --> l[3:]
print(output,"Index where we have added is",i)
