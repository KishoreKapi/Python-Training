class A:
    def move(self):
        print("I am moving.")  
class B(A): 
    def move(self):
        print("I am moving slowly.")  
x=A()
y=B()
x.move()
y.move()