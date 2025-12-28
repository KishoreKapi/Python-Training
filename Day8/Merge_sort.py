# l=[5,4,3,2,1,7,2]
l=[21,28,12,9,2,13,0]
def backtrack(lt):
    if(len(lt)==1):
        return lt
    l=backtrack(lt[0:len(lt)//2])
    r=backtrack(lt[len(lt)//2:])
    n=[]
    i,j=0,0
    while i<len(l) and j<len(r):
        if(l[i]<r[j]):
            n.append(l[i])
            i=i+1
        elif(l[i]>r[j]):
            n.append(r[j])
            j=j+1
        else:
            n.append(r[j])
            n.append(r[j])
            i=i+1
            j=j+1

    n=n+l[i:]
    n=n+r[j:]
    return n

f=backtrack(l)
print(f)