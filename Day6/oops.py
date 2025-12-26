class car:
    def __init__(self,name,wheels,gears,stearing,colour,engine):
        self.carname=name
        self.wheels=wheels
        self.gears=gears
        self.stearing=stearing
        self.colour=colour
        self.engine=engine
    
    def move(self):
        print(self.carname,"Car is moving")
    def slow(self):
        print("Car is getting slow")
        
    def get_colour(self):
        print("Car colour is ",self.colour)
    
    def get_gears(self):
        print("Car have ",self.gears," gears")

toyoto=car("Toyoto",4,5,1,"white",1)
BMW=car("BMW",4,5,1,"Black",1)

scg=car("scg",4,6,1,"blue",2)

toyoto.move()
BMW.move()
scg.get_colour()
print(scg.engine)
print(toyoto.gears)

