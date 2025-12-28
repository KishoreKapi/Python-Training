class Node:
    def __init__(self,val=None,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
    
    def __str__(self):
        # return f"{self.val}"
        return str(self.val)

a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
e=Node(5)
f=Node(6)
g=Node(7)
h=Node(8)
i=Node(9)

a.left=b
a.right=c
b.left=d
b.right=e
c.left=f
c.right=g
d.left=h
e.left=i

#DFS PreOrder (by using iteration)


l=[a]
f=[]

while l:
    last_item=l.pop()
    if(not last_item):
        continue
    f.append(last_item.val)
    l.append(last_item.right)
    l.append(last_item.left)
print(f," --PreOrder Iterative")

#DFS PreOrder (by using recurrsion)
f=[]

def PreOrder_Recc(val):
    if(not val):  # Base Condition
        return
    f.append(val.val)
    PreOrder_Recc(val.left)
    PreOrder_Recc(val.right)

PreOrder_Recc(a)

print(f," --PreOrder recurrsion")
    
#DFS InOrder (by using recurrsion)
f=[]

def InOrder_Recc(val):
    if(not val):
        return
    InOrder_Recc(val.left)
    f.append(val.val)
    InOrder_Recc(val.right)

InOrder_Recc(a)

print(f," --InOrder recurrsion")

#DFS PostOrder (by using recurrsion)

f=[]

def PostOrder_Recc(val):
    if(not val):
        return
    PostOrder_Recc(val.left)
    PostOrder_Recc(val.right)
    f.append(val.val)

PostOrder_Recc(a)

print(f," --PostOrder recurrsion")
    
# BFS

from collections import deque

f=[]

q=deque()
q.append(a)    

while q:
    first_item=q.popleft()
    if(not first_item):
        continue
    f.append(first_item.val)
    q.append(first_item.left)
    q.append(first_item.right)

print(f," --BFS")


# Check If value Exists DFS

def check(node,target):
    if(not node):
        return False
    if(node.val==target):
        return True

    return check(node.left,target) or check(node.right,target)

print(check(a,25))
print(check(a,5))