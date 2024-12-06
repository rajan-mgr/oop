# class Employee():
#     def __init__(self,name,department,salary):
#         self.name=name
#         self._department=department
#         self.__salary=salary
        
#     # def get_salary(self): #making a function so we can call it from outside of class
#     #     return self.__salary   
#     def __validate_salary(self,newsalary):
#         if newsalary<=0:
#             raise ValueError("Salary must be positive")
#     @property
#     def salary(self):
#             return self.__salary 
        
#     @salary.setter    
#     def salary(self,newsalary): #was set_salary preiously
#         if newsalary>0:
#             self.__salary=newsalary
#         else:
#             raise ValueError("Salary must be positive")  #raise can raise expectional in this case error
        
          
#     # salary=property(get_salary,set_salary) 
#     def employee_detail(self):     #making function to call private attribute
#         print("Name:",self.name)
#         print("Department:",self._department)
#         print("Salary:",self.__salary)        
            
        
        
# e=Employee("Ram","Marketing",25000)
# e.salary=90000
# # e.set_salary(40000)
# e.employee_detail()
# # print(e.get_salary())
# print(e.salary) 










'''
e.name="Shyam" #public attribute can be updated outside of class
e.__salary=90000 #private cannot be changed


print(e.name)
print(e._department)  
print(e.__salary)  '''  
#Private cannot be accesed from outside of class  
class Employee():
    def __init__(self,name,department,salary):
        self.name=name
        self._department=department
        self.__salary=salary
        
    def _update_department(self,new_department):
        self._department=new_department
        
    def change_department(self,new_department):
        self._update_department(new_department)    
        

    def __validate_salary(self,newsalary):
        if newsalary<=0:
            raise ValueError("Salary must be positive")
    @property
    def salary(self):
            return self.__salary 
        
    @salary.setter    
    def salary(self,newsalary): 
        self.__validate_salary(newsalary)
        self.__salary=newsalary
        
      
    def employee_detail(self):  
        print("Name:",self.name)
        print("Department:",self._department)
        print("Salary:",self.__salary)        
            
        
        
e=Employee("Ram","Marketing",25000)
e.salary=20
e.change_department("Finace")
e.salary=9090
# e._update_department("Finace")
e.employee_detail()