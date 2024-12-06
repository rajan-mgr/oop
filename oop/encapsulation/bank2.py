class BankAccount:
    def __init__(self, account_holder, account_type, initial_balance=0):
        self.account_holder = account_holder
        self._account_type = account_type
        self.__balance = initial_balance

    def display_account_details(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Type: {self._account_type}")
        print(f"Current Balance: Rs{self.__balance}")

    def _update_account_type(self, new_type):
        self._account_type = new_type

    def deposit(self, amount):
        if self.__validate_transaction(amount):
            self.__balance += amount
            print(f"Deposited: Rs{amount}. New Balance: Rs{self.__balance}")

    def withdraw(self, amount):
        if self.__validate_transaction(amount):
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew: Rs{amount}. New Balance: Rs{self.__balance}")
            else:
                print("Insufficient funds for this withdrawal.")

    def __validate_transaction(self, amount):
        if amount <= 0:
            print("Transaction amount must be positive.")
            return False
        return True

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if self.__validate_transaction(amount):
            self.__balance = amount
            print(f"Balance updated to: Rs{self.__balance}")
        else:
            print("Invalid balance amount.")

account = BankAccount("Rajan", "Savings", 1000)
account.display_account_details()
account.deposit(500)
account.withdraw(200)
account.withdraw(1500)
account.balance = 2000
print(f"Updated Balance via property: Rs{account.balance}")
