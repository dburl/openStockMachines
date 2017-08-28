from marketsim.TimeKeeper import TimeUtils
from marketsim.Constants import CCYMARKET, CCY
from Logger import *
"""
OrderBase: base class for an Exchange order
"""
class OrderBase:
    _ID = 1
    def __init__(self):
        self.id=self._ID
        self._ID += 1
        self.expired = False
        self.market_key_inverse = False
        self.market_key = None
        self.market = None
        self.payer_acc = None
        self.payee_acc = None

    def update(self, time, markets):
        self.__check_market_inversion()

    def expire(self):
        self.expired = True

    def is_expired(self):
        return self.expired

    def __check_market_inversion(self):
        try:
            market = CCYMARKET(self.market_key)
            self.market = market
        except:
            try:
                market = CCYMARKET(self.market_key[::-1])
                self.market_key_inverse = True
                self.market = market
            except:
                print("Order failed, invalid market key")
        finally:
            if self.market_key_inverse:
                self.payee_acc, self.payer_acc = self.payer_acc, self.payee_acc

"""
MarketOrder: order to buy a pair market_key
"""
class MarketOrder(OrderBase):
    def __init__(self, market_key, qty, payer_acc = None, payee_acc=None):
        OrderBase.__init__(self)
        self.market_key = market_key
        self.qty = qty
        self.payer_acc = payer_acc
        self.payee_acc = payee_acc
        get_global_log().info("Order#" + str(self.id) + " is created")

    def with_accounts(self, accounts):
        self.payer_acc = accounts[self.market_key.value[1]]
        self.payee_acc = accounts[self.market_key.value[0]]

    def update(self, time, markets):
        OrderBase.update(self, time, markets)
        if (type(self.market) is CCYMARKET) and (self.market in markets.keys()):
            self.market_price = markets[self.market].get_market_price(time)
            if self.market_price is not None:
                if self.market_key_inverse:
                    self.market_price = 1/self.market_price
                # execute the order
                market_value = self.market_price * self.qty
                self.payer_acc.debit(self.qty)
                self.payee_acc.credit(market_value)
                OrderBase.expire(self)  # mark as executed
                get_global_log().info("Order#"+str(self.id)+" is executed: "+self.__str__())
        else:
            get_global_log().error("Market key is not present at Exchange")
