from marketsim.TimeKeeper import TimeUtils
from marketsim.Constants import CCYMARKET, CCY
from marketsim.Exchange import BuyOrder

"""
InfMonthlyStandingOrder: infinite monthly standing order
"""
class Strategy:
    def execute(self, accounts, observe_fun, time):
        return []

class MonthlySalary(Strategy):
    def __init__(self, ccy, qty):
        self.ccy=ccy
        self.qty=qty
    def execute(self, accounts, observe_func, time):
        if (TimeUtils.isEOM(time)):
            accounts[self.ccy].credit(self.qty)
        return []

class BuyEuros(Strategy):
    def execute(self, accounts, observe_func, time):
        orders = []
        for acc in accounts:
            if acc.ccy is not CCY.GBP:
                orders.append(BuyOrder((acc.ccy, CCY.EUR), acc.balance(), acc, accounts[CCY.EUR]))
        return orders

