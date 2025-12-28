# Write a python programme to find min and max values of list?

l=[4,3,6,12,9,7,21,0,78]

min_val=100000
max_val=0

for i in range(0,len(l),1): #i=2
    if(l[i]<min_val): #6<3
        min_val=l[i] #min_val=3
    if(l[i]>max_val): #6>4
        max_val=l[i] # max_val=6
        
        
print("Minimum Value is",min_val)
print("Maximum Value is",max_val)

# print(min(l))
# print(max(l))
