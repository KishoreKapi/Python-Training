class Node:
    def __init__(self,val,left=None,right=None):
        self.left=left
        self.val=val
        self.right=right
        
    def __str__(self):
        return str(self.val)
a=Node(1)
# print(type(a))
# print(type(a.val))
# print(type(a.left))
# print(type(a.right))
# b="1"
# print(type(b))
b=Node(2)
c=Node(3)
a.right=b
b.left=a
b.right=c
c.left=b
print(a,a.left,a.right)
print(b,b.left,b.right)
print(c,c.left,c.right)
print("-----------------------")
#circular linked list
c.right=a
a.left=c
print(a,a.left,a.right)
print(b,b.left,b.right)
print(c,c.left,c.right)