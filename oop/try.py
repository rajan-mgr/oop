class Account():
    def __init__(self,name,accountno,password):
        self.name=name
        self.accountno=accountno
        self.password=password
        self.balance=0
    
    def personal_info(self,accountno,password):
        
        if self.accountno==accountno and self.password==password:
            print(f"Name={self.name}")
            print(f"Account No={self.accountno}")
            print(f"Balance={self.balance}")     
            
        else:
            print("Invalid Information")   
              
    def add_balance(self,accountno,name,balance):
        if self.accountno==accountno and self.name==name and balance>0:
            self.balance+=balance
            print(f"New balance is {self.balance}") 
        else:
            print("Cannnot be added")    
            
    def withdraw_balance(self,accountno,password,withdraw):
        if  self.accountno==accountno and self.password==password and withdraw>0:
            self.balance-=withdraw  
            print(f"Amount withdraw is {self.balance}")    
        else:
            print("Cannot withdraw")        
users={}
while 1:
    print("Enter 1 to create your account")
    print("Enter 2 to see your account information")
    print("Enter 3 to add balance:")
    print("Enter 4 to withdraw :")
    print("Enter 0 to exit:")
    a=int(input("Enter your decision:"))
    
    if a == 1:
        name=input("Enter your name:")
        password=input("Enter your password:")
        accountno=int(input("Enter your account No:"))
        if accountno in users:
            print("The accno is not avaible.")
        else:
            users[accountno]=Account(name,accountno,password)  
        
    elif a == 2:
        accountno=int(input("Enter your account no:"))
        password=input("Enter your password:")
        if accountno in users:
            users[accountno].personal_info(accountno,password)
        else:
            print("Create an account first")  
    elif a == 3:
        name=input("Enter your name:")
        accountno=int(input("Enter your accountno:"))
        balance=int(input("Enter the amount you want to add:"))
        if accountno in users:
            users[accountno].add_balance(accountno,name,balance)
        else:
            print("Create an account first")  

    elif a == 4:
        accountno=int(input("Enter your accnount no:"))
        password=input("Enter your password:")
        withdraw=int(input("Enter the amount you want to withdraw:"))
        if accountno in users:
            users[accountno].withdraw_balance(accountno,password,withdraw)
        else:
            print("Create an account first")    
            
    elif a == 0:
        break        
    else:
        print("Invalid option")