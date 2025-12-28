class Node:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next
    def __str__(self):
        return str(self.val)

a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
# print(a.val)
# print(a.next)
# print(a)
# print(b)
# print(b.val)
a.next=b
b.next=c
c.next=d
print(a)
print(a.next)
print(c.next)
print(d.next)

        