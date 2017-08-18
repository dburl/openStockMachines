from marketsim.TimeKeeper import TimeUtils
from marketsim.Constants import CCYMARKET, CCY

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
        market = None
        inverse=False
        try:
            market = CCYMARKET(self.market_key)
        except:
            try:
                market = CCYMARKET(self.market_key[::-1])
                inverse=True
            except:
                print("BuyOrder failed, invalid market key")
        finally:
            if (type(market) is CCYMARKET) and (market in markets.keys()):
                self.market_price = markets[market].get_market_price(time)
                if self.market_price is not None:
                    if inverse:
                        self.market_price=1/self.market_price
                    self.market_value = self.market_price * self.qty
                    self.payer_acc.debit(self.qty)
                    self.payee_acc.credit(self.market_value)
                    Order.expire(self)
            else:
                print("Market key is not present at Exchange")
