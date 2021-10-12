import datetime

class Transaction:
    def __init__(self, date: str, type: str, amount: int):
        self.date = date
        self.type = type # Either 'w' (withdraw) or 'd' (deposit)
        self.amount = amount

    def getDate(self):
        return self.date

    def getType(self):
        return self.type

    def getAmount(self):
        return self.amount

    def toDict(self):
        """Returns a dictionary version of the Transaction object."""

        transactionDict = {
            "date": self.date,
            "type": self.type,
            "amount": self.amount
        }

        return transactionDict