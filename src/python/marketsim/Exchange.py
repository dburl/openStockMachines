from marketsim.TimeKeeper import TimeUtils

"""
Order: base class for an Exchange order
"""
class Order:
    def __init__(self):
        self.expired = False
    def update(self, time, markets):
        raise NotImplementedError("update not implemented by child class yet")
    def expire(self):
        self.expired = True
    def is_expired(self):
        return self.expired

"""
InfMonthlyStandingOrder: inifinte monthly standing order
"""
class InfMonthlyStandingOrder(Order):
    def __init__(self, ccy, qty, payee_acc):
        Order.__init__(self)
        self.ccy = ccy
        self.qty = qty
        self.payee_acc = payee_acc
    def update(self, time, markets):
        if(TimeUtils.isEOM(time)):
            self.payee_acc.credit(self.qty)

"""
BuyOrder: order to buy a currency
"""
class BuyOrder(Order):
    def __init__(self, market_key, qty, payer_acc, payee_acc):
        Order.__init__(self)
        self.market_key = market_key
        self.qty = qty
        self.payer_acc = payer_acc
        self.payee_acc = payee_acc
    def update(self, time, markets):
        if(self.market_key not in markets.keys()):
            print("BuyOrder failed, invalid market key")
        else:
            self.market_price = markets[self.market_key].get_market_price(time)
            self.market_value = self.market_price * self.qty
            self.payer_acc.debit(self.qty)
            self.payee_acc.credit(self.market_value)
        Order.expire(self)


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
    def __str__(self):
        return "{} - {}".format(self.ccy, self.bal)
"""
Exchange: holds and executes orders
"""
class Exchange:
    def __init__(self, market_models, init_orders):
        self.markets = market_models
        self.orders = init_orders
    def add_order(self, order):
        self.orders.append(order)
    def update(self,time):
        for nxt in self.orders:
            nxt.update(time, self.markets)
        self.orders = list(filter(lambda x: not x.is_expired(), self.orders))
