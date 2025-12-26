def fun(*values,**key_values):
    print(values)
    print(key_values)
        
fun(5,6,7,8,a=1,b=2)
print("--------------------")
fun(1,2,f=1,x=2,h=6)

print("--------------------")
fun(w=1,y=2)
print("--------------------")
fun(50,60)