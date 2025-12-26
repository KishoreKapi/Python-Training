class A:
    def move(self):
        print("I am moving.")
    
    def sleep(self):
        print("I am sleeping.")
        
class B(A):
    def walk(self):
        print("I am walking.")
        
    def move(self):
        print("I am moving slowly.")
        super().move() #A.move()

class C(B):
    def write(self):
        print("I am writing.")
        
x=B()
x.move()

y=A()
y.move()

z=C()
z.sleep()