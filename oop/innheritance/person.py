class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def is_sleeping(self):
        print(f"{self.name} is sleeping")
        
class Student(Person): #inheritate from person
    def __init__(self,name,age,ID,grade):
        super().__init__(name,age) #super() represent parent class
        self.ID=ID
        self.grade=grade

    def is_studying(self):
        print(f"{self.name} is studying ")
        
    def is_sleeping(self):
        super().is_sleeping()
        print(f"{self.name} is sleeping")
        print("He is lazy")
        print("He is sleeping")   
        
        
student1=Student("Ram",18,123,12)
person1=Person("Shyam",16)
# print(student1.name)
# print(student1.grade) 
# print(student1.is_sleeping())       
# print(student1.is_studying())
# print(student1.is_studying())
# print(person1.is_studying())
print(student1.is_sleeping())
        