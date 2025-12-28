import heapq
l=[[1,4,5],[1,3,4],[2,6]]
s=[]
f=[]
for i in range(len(l)):
    s.append([l[i][0],i,0,len(l[i])-1])

heapq.heapify(s)

while s:
    min=heapq.heappop(s)
    f.append(min[0])
    if(min[2]<min[3]):
        heapq.heappush(s,[l[min[1]][min[2]+1],min[1],min[2]+1,min[3]])
    
print(f)
