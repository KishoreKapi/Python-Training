def fun(*values):
    print(values)
    for i in values:
        print(i)

        
fun(5,6,7,8)
print("--------------------")
fun(1,2)
  
fun(1,2,3)

class test :
    def hi(self,a = None,b = None, c =None) :
        if a != None and b != None and c != None :
            print(a + b + c)
        elif a != None and b != None :
            print(a+b)
            
        
c = test()
c.hi(10,20)
c.hi(10,20,30)