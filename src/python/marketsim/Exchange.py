from marketsim.TimeKeeper import TimeUtils
from marketsim.Constants import CCYMARKET, CCY

"""
Exchange: holds and executes orders
"""
class Exchange:
    markets = {}

    def __init__(self, market_model, init_orders=[]):
        self.markets[market_model.market_key] = market_model  # multiple markets are possible
        self.orders = init_orders

    def add_market(self, market_model, init_orders=[]):
        self.markets[market_model.market_key] = market_model  # multiple markets are possible
        self.orders.extend(init_orders)

    def add_order(self, order):
        self.orders.append(order)

    def get_pending_orders(self):
        return self.orders

    def update(self, time):
        for nxt in self.orders:
            nxt.update(time, self.markets)
        self.orders = list(filter(lambda x: not x.is_expired(), self.orders))
