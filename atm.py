import Bibliotek.spacebars as spacebars
from account import Account

class Atm:
    def __init__(self):
        self.isRunning = False # True if the atm is active. False otherwise.
        self.accountList = []
        self.currentAccount = None # The account that you are currently logged into.

    def accountExists(self, accountNumber: str):
        """Returns True if there exists an account with the given account number. Returns False otherwise."""

        exists = False

        for account in self.accountList:
            if account.getAccountNumber() == accountNumber:
                exists = True
                break

        return exists

    def createAccount(self):
        print("")
        print("Skapa konto")
        print("Skriv 'b' för att gå tillbaka.")
        print("------------------------------")
        
        while True:
            accountNumber = input("Kontonummer: ")

            if accountNumber == "b": # Go back back to the main menu by writing "b".
                break

            if not accountNumber.isdigit():
                print("Endast siffror är tillåtna.")
                continue

            if self.accountExists(accountNumber):
                print("Kontonummer upptaget.")
                continue

            account = Account(accountNumber)
            self.accountList.append(account)
            print("Konto skapat.")
            break

    def logIn(self): 
        print("")
        print("Logga in")
        print("Skriv 'b' för att gå tillbaka.")
        print("------------------------------")

        while True:
            accountNumber = input("Kontonummer: ")

            if accountNumber == "b": # Go back back to the main menu by writing "b".
                break

            if not accountNumber.isdigit():
                print("Endast siffror är tillåtna.")
                continue
            
            for account in self.accountList:
                if account.getAccountNumber() == accountNumber:
                    self.currentAccount = account
                    break
            
            if self.currentAccount == None: # If an account with the given account number does not exist.
                print("Kontot existerar inte.")
                continue

            print("Inloggning lyckades.")
            break
            

    def start(self):
        self.isRunning = True
    
    def end(self):
        self.isRunning = False
        print("Bankomaten avslutas.")

    def withdraw(self):
        print("")
        print("Ta ut pengar")
        print("Skriv 'b' för att gå tillbaka.")
        print("------------")

        amount = 0

        while True:
            amountString = input("Ange belopp: ")

            if amountString == "b": # Go back back to the account menu by writing "b".
                break

            try:
                amount = int(amountString)
            except:
                print("Skriv in ett positivt heltal, utan mellanslag.")
                continue

            if amount <= 0:
                    print("Beloppet måste vara positivt.")
                    continue

            if self.currentAccount.withdraw(amount):
                print("Pengar uttagna.")
                break
            else:
                print("För lågt saldo.")
                continue

    def deposit(self):
        print("")
        print("Sätt in pengar")
        print("Skriv 'b' för att gå tillbaka.")
        print("--------------")

        amount = 0

        while True:
            amountString = input("Ange belopp: ")

            if amountString == "b": # Go back back to the account menu by writing "b".
                break

            try:
                amount = int(amountString)
            except:
                print("Skriv in ett positivt heltal, utan mellanslag.")
                continue

            if amount <= 0:
                    print("Beloppet måste vara positivt.")
                    continue

            self.currentAccount.deposit(amount)
            print("Pengar insatta.")
            break
    

    def showBalance(self):
        balance = self.currentAccount.getBalance()

        print("")
        print("Saldo: " + str(balance) + " kr")

    def showTransactions(self):
        print("")
        print("Transaktioner")
        print("-------------")
        print("")
        print("Datum" + spacebars.spacebars(20) + "Typ" + spacebars.spacebars(20) + "Belopp (kr)")
        print("-" * 59)

        transactionList = self.currentAccount.getTransactionList()

        for transaction in transactionList:
            date = transaction.getDate()
            type = transaction.getType()
            amount = transaction.getAmount()

            if type == "w": # "w" stands for "withdraw."
                print(date + spacebars.spacebars(15) + "Uttag" + spacebars.spacebars(28 - len(str(amount))) + "-" + str(amount))
            elif type == "d": # "d" stands for "deposit."
                print(date + spacebars.spacebars(15) + "Insättning" + spacebars.spacebars(23 - len(str(amount))) + "+" + str(amount))
            else:
                print("Error: Invalid transaction type.")

    def logOut(self):
        self.currentAccount = None
        print("Du loggas ut.")

    def isLoggedIn(self):
        """Returns True if you are currently logged into an account. Returns False otherwise."""
        return self.currentAccount != None

    def mainMenu(self):
        
        print("")
        print("Olavs bankomat")
        print("--------------")

        print("1: Skapa konto")
        print("2: Logga in")
        print("3: Avsluta")
        print("")

        while True:
            alternative = input("Välj alternativ: ")

            if alternative == "1":
                self.createAccount()
                break

            elif alternative == "2":
                self.logIn()
                break
                
            elif alternative == "3":
                self.end()
                break

            else:
                print("Ogiltigt alternativ.")

    def accountMenu(self):

        accountNumber = self.currentAccount.getAccountNumber()
        
        print("")
        print("Konto " + accountNumber)
        print("-" * (6 + len(accountNumber)))

        print("1: Ta ut pengar")
        print("2: Sätt in pengar")
        print("3: Visa saldo")
        print("4: Visa transaktioner")
        print("5: Logga ut")
        print("")

        while True:
            alternative = input("Välj alternativ: ")

            if alternative == "1":
                self.withdraw()
                break

            elif alternative == "2":
                self.deposit()
                break

            elif alternative == "3":
                self.showBalance()
                break

            elif alternative == "4":
                self.showTransactions()
                break

            elif alternative == "5":
                self.logOut()
                break

            else:
                print("Ogiltigt alternativ.")

    def run(self):
        self.start()

        while self.isRunning:
            if self.isLoggedIn():
                self.accountMenu()
            else:
                self.mainMenu()

    def toDict(self):
        """Returns a dictionary version of the Atm object."""

        accountDictList = []

        for account in self.accountList:
            accountDictList.append(account.toDict())
        
        atmDict = {
            "accountList": accountDictList
            }

        return atmDict