class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def personal_info(self):
        print(f"This is {self.name} his age is {self.age}")
        
class Student(Person):
    def __init__(self,name,age,major,grade):
        super().__init__(name,age)
        self.major=major
        self.grade=grade
        
    def student_info(self):
        super().personal_info()   
        print(f"My major subject is {self.major}")   
        print(f"I study in {self.grade}")  
               
class Lecturer(Person):    
    def __init__(self,name,age,ID,salary,subject):
        super().__init__(name,age,ID,salary)
        self.subject=subject            
        self.ID=ID
        self.salary=salary
    def lecturer_info(self):
        super().personal_info()
        print(f"I teach {self.subject}")
        
S1=Student("Baniya",16,"Ethical Hacking","ETH35C") 
S1.student_info()      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# class Employee(Person):
#     def __init__(self,name,age,ID,salary):
#         super().__init__(name,age)
#         self.ID=ID
#         self.salary=salary
    
#     def employee_info(self):
#         super().personal_info()
#         print(f"ID number is:{self.ID}")
#         print(f"Salary is:{self.salary}")
        
# class Lecturer(Employee):
#     def __init__(self,name,age,ID,salary,subject):
#         super().__init__(name,age,ID,salary)
#         self.subject=subject
    
#     def lecturer_info(self):
#         super().employee_info()
#         print(f"I teach {self.subject}")           
                        
                        
# L1=Lecturer("Sumit",30,123,200000,"GETS") 
# L1.lecturer_info()      
             