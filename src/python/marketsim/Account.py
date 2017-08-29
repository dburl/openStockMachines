from Logger import *
"""
Account: holds a currency or equity
"""
class Account:
    def __init__(self, ccy):
        self.ccy = ccy
        self.bal = 0
    def credit(self, qty):
        self.bal += qty
        get_global_log().info("Account " + str(self.ccy) + " +" + str(qty))
    def debit(self, qty):
        if (self.bal-qty) < 0:
            get_global_log().warning("[Warning]\t Account "+ str(self.ccy)+" < 0 -> transaction is impossible")
            return False
        else:
            self.bal -= qty
            get_global_log().info("Account " + str(self.ccy) + " -"+str(qty))
            return True

    def balance(self):
        return self.bal
    def __str__(self):
        return "{} - {}".format(self.ccy, self.bal)