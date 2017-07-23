"""
InfMonthlyStandingOrder: inifinte monthly standing order
"""
class InfMonthlyStandingOrder:
    def __init__(self, ccy, qty, payee_acc):
        self.ccy = ccy
        self.qty = qty
        self.payee_acc = payee_acc
    def update(self):
        # TODO check datetime is end of month
        payee_acc.deposit(qty)

"""
BuyOrder: order to buy a currency
"""
class BuyOrder:
    def __init__(self, market_key, qty, payer_acc, payee_acc):
        pass
    def update(self):
        market_price = get_price(market_key)
        market_value = market_price * qty
        payer_acc -= qty
        payee_acc += market_value


"""
Account: holds a currency
"""
class Account:
    def __init__(self,ccy):
        self.ccy = ccy
        self.bal = 0
    def deposit(self,qty):
        self.bal += qty
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
            nxt.update()
