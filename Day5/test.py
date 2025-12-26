# d={"kishore":1,}
def fun(*values,**keyvalues):
    print(values)
    print(keyvalues)
    
fun(1,2,3,a=5,b=6)