import datetime
from transaction import Transaction

class Account:
    def __init__(self, accountNumber: str):
        self.accountNumber = accountNumber
        self.balance = 0
        self.transactionList = []
    
    def getAccountNumber(self):
        return self.accountNumber

    def getBalance(self):
        return self.balance

    def getTransactionList(self):
        return self.transactionList

    def logTransaction(self, type: str, amount: int): # Type is either 'w' (withdraw) or 'd' (deposit).
        currentDate = str(datetime.date.today())
        transaction = Transaction(currentDate, type, amount)
        self.transactionList.append(transaction)

    def withdraw(self, amount: int):
        """If the given amount is less than or equal to the current balance, the balance is decreased by that amount and the function returns True. Returns False otherwise."""
        if amount <= self.balance:
            self.balance -= amount
            self.logTransaction("w", amount) # "w" stands for "withdraw".
            return True
        else: 
            return False

    def deposit(self, amount: int):
        self.balance += amount
        self.logTransaction("d", amount) # "d" stands for "deposit".

    def toDict(self):
        """Returns a dictionary version of the Account object."""

        transactionDictList = []

        for transaction in self.transactionList:
            transactionDictList.append(transaction.toDict())
        
        accountDict = {
            "accountNumber": self.accountNumber, 
            "balance": self.balance,
            "transactionList": transactionDictList
            }

        return accountDict