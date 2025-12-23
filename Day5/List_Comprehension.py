l=[1,2,3,4,5]
for i in l:
    print(i*i)

print([i*i for i in l if i%2!=0])

d={"a":1,"b":2,"c":3,"d":4,"e":5}
for key,value in d.items():
    print(key,value*value)

f={key:val for key,val in d.items() if val%2!=0}
print(f)