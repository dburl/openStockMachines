from marketsim.TimeKeeper import TimeUtils
from marketsim.Constants import CCYMARKET, CCY
from marketsim.Order import BuyOrder

"""
InfMonthlyStandingOrder: infinite monthly standing order
"""
class Strategy:
    def execute(self, accounts, observe_fun, time):
        return []

class MonthlySalary(Strategy):
    def __init__(self, ccy, qty):
        self.ccy = ccy
        self.qty = qty
    def execute(self, accounts, observe_func, time):
        if (TimeUtils.isEOM(time)):
            accounts[self.ccy].credit(self.qty)
        return []

class BuyEuros(Strategy):
    def execute(self, accounts, observe_func, time):
        orders = []
        for acc_key, acc_value in accounts.items():
            if acc_key is not CCY.EUR and (acc_value.balance() != 0):
                orders.append(BuyOrder((acc_key, CCY.EUR), acc_value.balance(), acc_value, accounts[CCY.EUR]))
        return orders

