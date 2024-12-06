class Account():
    def __init__(self,name,passwd,accountno):
        self.name=name
        self.passwd=passwd
        self.accountno=accountno
        self.balance=0
 
    def display_info(self,accountno,passwd):
        if self.accountno == accountno and self.passwd == passwd:
            print(f"Name:{self.name}")  
            print(f"Account Number:{self.accountno}")  
            print(f"Avaiable Balance:{self.balance}")
        else:
            print("Invalid Credentials")
    
    def add_balance(self,accountno,balance):
        if self.accountno == accountno and balance>0:
            self.balance=self.balance+balance
        else:
            print("Cannot be deposited")        
    
    def withdraw(self,accountno,passwd,withdraw):
        if self.accountno == accountno and self.passwd == passwd and self.balance>=withdraw:
            self.balance=self.balance-withdraw
            print("Amount withdrawn:",withdraw)
        else:
            print("You are poor")    
        
                
users={}
while True:
    print("Enter 1 to create account:")
    print("Enter 2 to see information:")
    print("Enter 3 to add balance:")
    print("Enter 4 to withdraw balance:")
    print("Enter 0 to exit:")          
      
    choice=input("Enter your choice:")
    if choice == '1':
        name = input("Enter your name:")
        passwd = input("Enter your password:")
        accountno = input("Enter your account number:")
        
        if accountno in users:
            print("This account number is not available. Please choose another.")
        else:
            users[accountno] = Account(name, passwd, accountno)
            print("Account created successfully.")
        
    elif choice == '2':
        accountno = input("Enter your account number:")
        passwd = input("Enter your password:")
        if accountno in users:
            users[accountno].display_info(accountno, passwd)
        else:
            print("Account not found.")
        
    elif choice == '3':
        accountno = input("Enter your account number:")
        balance = int(input("Enter amount to add:"))
        if accountno in users:
            users[accountno].add_balance(accountno, balance)
        else:
            print("Account not found.")
    
    elif choice == '4':
        accountno = input("Enter your account number:")
        passwd = input("Enter your password:")
        withdraw = int(input("Enter your amount to withdraw:"))
        if accountno in users:
            users[accountno].withdraw(accountno, passwd, withdraw)
        else:
            print("Account not found.")
        
    elif choice == '0':
        break
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
