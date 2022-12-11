Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Account:
...     def __init__(self, title=None, balance=0):
...         self.title = title
...         self.balance = balance
...     
...     def withdrawal(self, amount):
...         # write code here
...         pass
... 
...     def deposit(self, amount):
...         # write code here
...         pass
...     def getBalance(self):
...         # write code here
...         pass
... 
... class SavingsAccount(Account):
...     def __init__(self, title=None, balance=0, interestRate=0):
...             super().__init__(title, balance)
...             self.interestRate = interestRate
...     
...     def interestAmount(self):
...         # write code here
...         pass
... 
... #code to test - do not edit this
... 
