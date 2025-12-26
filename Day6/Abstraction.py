from abc import ABC,abstractmethod

class A(ABC):
    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def walk(self):
        pass

class B(A):
    def move(self):
        print("I am moving.")
    
    def walk(self):
        print("I am walking.")
    
    def write(self):
        print("I am writing.")

y=B()
y.move()
y.walk()
y.write()