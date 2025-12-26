class A:
    def __init__(self,a,b):
        self.__c=a
        self.d=b
    def add(self):
        print(self.__c+self.d)
    
    def __sub(self):
        print(self.__c-self.d)
    
    def diff(self):
        self.__sub()
    
    @property 
    def p(self):
        return self.__c
    
    @p.setter
    def p(self,value):
        self.__c=value

x=A(5,3)
print(x.d)
# print(x.__c)
# x.__sub()
x.diff()
print(x.p)
x.p=10
print(x.p)
