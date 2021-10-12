from transaction import Transaction

def dictToTransaction(transactionDict: dict):
    """Returns a Transaction object corresponding to its given dictionary version."""

    return Transaction(transactionDict["date"], transactionDict["type"], transactionDict["amount"])
