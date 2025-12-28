a=[] #stack
a.append(1)
a.append(2)
a.append(3)
print(a)
a.pop()
print(a)

from collections import deque

b=deque()
print(b)
b.append(1)
b.append(2)
b.append(3)
print(b)
b.popleft()
print(b)
b.appendleft(10)
print(b)