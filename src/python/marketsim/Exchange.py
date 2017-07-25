from marketsim.TimeKeeper import TimeUtils
"""
InfMonthlyStandingOrder: inifinte monthly standing order
"""
class InfMonthlyStandingOrder:
    def __init__(self, ccy, qty, payee_acc):
        self.ccy = ccy
        self.qty = qty
        self.payee_acc = payee_acc
    def update(self, time):
        if(TimeUtils.isEOM(time)):
            self.payee_acc.credit(self.qty)

"""
BuyOrder: order to buy a currency
"""
class BuyOrder:
    def __init__(self, market_key, qty, payer_acc, payee_acc):
        self.market_key = market_key
        self.qty = qty
        self.payer_acc = payer_acc
        self.payee_acc = payee_acc
    def update(self, time):
        self.market_price = 1.2#get_price(self.market_key)  #TODO need to lookup a ticker here for current price
        self.market_value = self.market_price * self.qty
        self.payer_acc.debit(self.qty)
        self.payee_acc.credit(self.market_value)


"""
Account: holds a currency
"""
class Account:
    def __init__(self,ccy):
        self.ccy = ccy
        self.bal = 0
    def credit(self,qty):
        self.bal += qty
    def debit(self,qty):
        self.bal -= qty
    def balance(self):
        return self.bal
"""
Exchange: holds and executes orders
"""
class Exchange:
    orders=[]
    def __init__(self, init_orders):
        self.orders = init_orders
    def add_order(self, order):
        self.orders.append(order)
    def update(self,time):
        for nxt in self.orders:
            nxt.update(time)
