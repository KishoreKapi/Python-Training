l1=[1,2,5]
        # ^
        # i
l2=[1,3,4]
      # ^
      # j
# output=[1,1,2,3,4,4]
output=[]
i,j=0,0
while i<len(l1) and j<len(l2):
    if(l1[i]<=l2[j]):
        output.append(l1[i])
        i=i+1
    else:
        output.append(l2[j])
        j=j+1

# print(output)
output=output+l1[i:]
output=output+l2[j:]

print(output)


