from dict_to_transaction import dictToTransaction
from account import Account
from dict_to_transaction import dictToTransaction

def dictToAccount(accountDict: dict):
    """Returns an Account object corresponding to its given dictionary version."""

    accountNumber = accountDict["accountNumber"]
    balance = accountDict["balance"]
    transactionList = []

    for transactionDict in accountDict["transactionList"]:
        transaction = dictToTransaction(transactionDict)
        transactionList.append(transaction)

    account = Account(accountNumber)
    account.balance = balance
    account.transactionList = transactionList

    return account