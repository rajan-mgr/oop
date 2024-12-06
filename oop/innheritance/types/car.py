class Car():
    def __init__(self,color,fuel):
        self.color=color
        self.fuel=fuel
    
    def is_moving(self):
        print(f"A {self.color} color car is moving")
        print(f"it's fuel capacity is {self.fuel}")
            
class ElectricAppliance():
    def __init__(self,battery):
        self.battery=battery
    
    def is_charging(self):
        print(f"The battery of {self.battery} KWH is charging")                
        
class Hybrid_car(Car,ElectricAppliance):
    def __init__(self,fuel,color,battery):
        Car.__init__(self,color,fuel)
        ElectricAppliance.__init__(self,battery)
    
    def display_info(self):
        print("This is  a hybrid car")
        print("Battery Capacity:",self.battery)
        print("Fuel Capacity",self.fuel)    

h1=Hybrid_car("50l",'White',100)
h1.display_info()
h1.is_moving()
h1.is_charging()
print(h1.color)