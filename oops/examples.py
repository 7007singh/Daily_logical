from abc import ABC, abstractmethod


# 🔹 Abstraction
class Account(ABC):
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance  # 🔐 Encapsulation (private)

    # Encapsulation (getter)
    def get_balance(self):
        return self.__balance

    # Encapsulation (method control)
    def deposit(self, amount):
        self.__balance += amount

    @abstractmethod
    def withdraw(self, amount):
        pass


# 🔹 Inheritance + Polymorphism
class SavingsAccount(Account):
    def withdraw(self, amount):
        if amount <= self.get_balance():
            print("Savings Withdraw:", amount)
        else:
            print("Insufficient balance")


class CurrentAccount(Account):
    def withdraw(self, amount):
        print("Current Withdraw:", amount)


# 🔹 Using polymorphism
accounts = [SavingsAccount("Rahul", 1000), CurrentAccount("Aman", 2000)]

for acc in accounts:
    acc.withdraw(500)
