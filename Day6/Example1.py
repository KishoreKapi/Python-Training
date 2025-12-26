class sum:
    def __init__(self,a,b):
        self.c=a
        self.d=b
    def getsum(self):
        print(self.c+self.d)
        
x=sum(2,3)
y=sum(5,4)
y.getsum()
x.getsum()