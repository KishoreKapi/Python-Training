path="data.csv"
file=open(path,'r')
output=file.read()
file.close()
print(output)

file=open(path,'a+')
file.write("\nshivani,22")
output=file.read()
file.close()
print(output)


with open(path,'r') as f:
    output=f.read()

print(output)

with open(path,'a+') as f:
    f.write("\nkarthik,\"21\"")
    output=f.read()
print(output)
    

