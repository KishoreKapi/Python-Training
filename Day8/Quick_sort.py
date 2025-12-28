l=[5,4,3,2,1,7,2,-7,-9]

def quick_sort(lt):
    if(len(lt)<=1):
        return lt
    p=lt[-1]
    l=[]
    r=[]
    for i in range(len(lt)-1):
        if(lt[i]<=p):
            l.append(lt[i])
        else:
            r.append(lt[i])
    return quick_sort(l)+[p]+quick_sort(r)
    
f=quick_sort(l)
print(f)