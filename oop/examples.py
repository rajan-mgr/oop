#Example1:
class Student():
    college="Softawrica"
    stream="Ethical"
    subject="Programming"

    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.selfstudy=False


    def does_self_study(self):
        self.selfstudy=True   

    def display_study_status(self):
        if self.selfstudy:
            print(f"{self.name},student of {self.college} does self study of {self.subject} ")
        else:
            print(f"{self.name}, student of {self.college} never does self study of {self.subject}")

student1=Student("Roshan",20)
student2=Student("Hero",19)
student1.does_self_study()
student1.display_study_status()
student2.display_study_status()

#Example2:

class Car():
    wheel_count=4
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
        self.status="not moving"
        self.gear=0
    
    def start_car(self):
        self.status="moving"
        self.gear=1
    
    def change_gear(self,new_gear):
        if self.status=="moving":
            self.gear=new_gear
        else:
            print(f"We cannot change gear without starting car")
            self.gear=0
            
    def display_car_status(self):
        print(f"{self.brand} is {self.status} and gear is {self.gear}")
                            
    def car_info(self):    
        print(f"Brand:{self.brand}")
        print(f"Color:{self.color}")
        print(f"Status:{self.status}")
        print(f"Gear number:{self.gear}")
        
car1=Car("Toyata","White")
car1.start_car()
car1.change_gear(4)
car1.car_info()        