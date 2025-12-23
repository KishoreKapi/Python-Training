l=[1,2,3,4,5]
print(*l)
l=(1,2,3,4,5)
print(*l)
l={1,2,3}
print(*l)
# d={"a":1,"b":2,"c":3,"d":4,"e":5}
def test(**d):
    print(d)

test(a=1,b=2)
