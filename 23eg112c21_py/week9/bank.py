# 3. Create a class BankAccount with private attributes __account_number and __balance.
# Implement public methods to get the balance (get_balance()), deposit money
# (deposit(amount)), and withdraw money (withdraw(amount)).

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance.")

# Example usage:
account = BankAccount("1234567890", 1000)
print(account.get_balance())  # Output: 1000

account.deposit(500)
print(account.get_balance())  # Output: 1500

account.withdraw(200)
print(account.get_balance())  # Output: 1300

account.withdraw(2000)  # Output: Insufficient balance.
print(account.get_balance())  # Output: 1300