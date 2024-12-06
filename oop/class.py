class Student():
    def __init__(self,name,age,major):    #s1,s2 (object)is passed into self
        self.name=name
        self.age=age
        self.major=major

    def is_studying(self):
        print(f"{self.name} is studying {self.major} subject")

s1=Student("Rajan",19,"Hacking")
s2=Student("Sanil",20,"Programming")

print(s1.name,s1.major) #printing property
s2.is_studying() #printing behavior

class Car():
    def __init__(self,name,speed):
        self.name=name
        self.speed=speed
    def is_moving(self):
        print(f"{self.name} is moving at {self.speed}")
        
car1=Car("Suzuki","30km/h")
car2=Car("BMW","80km/h")   

print(car1.name)
car1.is_moving()             