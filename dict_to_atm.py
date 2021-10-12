from atm import Atm
from dict_to_account import dictToAccount

def dictToAtm(atmDict: dict):
    """Returns an Atm object corresponding to its given dictionary version."""

    accountList = []

    for accountDict in atmDict["accountList"]:
        account = dictToAccount(accountDict)
        accountList.append(account)

    atm = Atm()
    atm.accountList = accountList

    return atm