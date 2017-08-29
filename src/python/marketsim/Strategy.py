from marketsim.TimeKeeper import TimeUtils
from marketsim.Constants import CCYMARKET, CCY
from marketsim.Order import MarketOrder, SellOrder, BuyOrder
from Logger import *
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
            get_global_log().info("Account " + str(self.ccy) + ": salary income of "
                                  + str(self.qty)+time.strftime(" @ %Y-%m-%d"))
        return []

class BuyEuros(Strategy):
    def execute(self, accounts, observe_func, time):
        orders = []
        for acc_key, acc_value in accounts.items():
            if acc_key is not CCY.EUR and (acc_value.balance() != 0):
                get_global_log().info("[BuyEuros] new order " + time.strftime(" @ %Y-%m-%d"))
                market_key = (acc_key, CCY.EUR)
                new_order = SellOrder(market_key, acc_value.balance(), accounts)
                orders.append(new_order)
        return orders

