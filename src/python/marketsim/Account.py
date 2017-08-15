"""
Account: holds a currency/equity
"""
class Account:
    def __init__(self, ccy):
        self.ccy = ccy
        self.bal = 0
    def credit(self,qty):
        self.bal += qty
    def debit(self,qty):
        if (self.bal-qty)<0:
            print("Transaction is impossible")
            return False
        else:
            self.bal -= qty
            return True

    def balance(self):
        return self.bal
    def __str__(self):
        return "{} - {}".format(self.ccy, self.bal)