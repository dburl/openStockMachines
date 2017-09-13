from marketsim.TimeKeeper import TimeUtils
from marketsim.Constants import CCYMARKET, CCY
from Logger import *
"""
OrderBase: base class for an Exchange order
"""
class OrderBase:
    _ID = 1  # orders counter [#]1, 2, 3,...
    def __init__(self):
        self.id = OrderBase._ID  # unique id for each order
        OrderBase._ID += 1
        self.expired = False  # when True, order is not pending anymore and does not require execution
        self.market_key_inverse = False  # True if market_key is inverted to get quote
        self.market_key = None  # key =(to_buy, to_pay_from)
        self.market = None  # deducted(if exists) from market_key
        self.payer_acc = None
        self.payee_acc = None
        self.market_price = None  # price at which the order is executed
        self.expiration_date = None

    def expire(self):
        self.expired = True

    def set_expiraton_date(self, date):  # if not explicitly set, the date is EOF of order creation
        self.expiration_date = date

    def is_expired(self):
        return self.expired

    def __str__(self):
        return "order {}:{}".format(str(self.id), str(self.market_key))

    def update(self, time, markets):
        self.__check_market_inversion()
        self.__check_if_pending(time)

        ## Sanity checks
        # if one of the accounts is not set properly
        if self.payer_acc is None or self.payee_acc is None:
            get_global_log().error("[Error]\t Accounts for order are not set")
            raise
        #if the requested market does not exist
        if not (type(self.market) is CCYMARKET) and (self.market in markets.keys()):
            get_global_log().error("[Error]\t Market key is not present at Exchange")
            raise


    def __check_if_pending(self, time):
        if self.expiration_date is None:
            self.set_expiraton_date(time)  # at least we try once
        if time > self.expiration_date:
            self.expire()
            get_global_log().info("order {} (exp date {}) expired @ {}".format(str(self.id), \
                                self.expiration_date.strftime("%Y-%m-%d"), time.strftime("%Y-%m-%d")))
        return self.is_expired()

    def __check_market_inversion(self):
        try:
            market = CCYMARKET(self.market_key)
            self.market = market
        except:
            pass

        try:
            market = CCYMARKET(self.market_key[::-1])
            self.market_key_inverse = True
            self.market = market
        except:
            pass
        if self.market is None:
            get_global_log().error("[Error]\t Order failed, invalid market key")
            raise

"""
MarketOrder: order to buy a pair market_key = (equity_to_buy,account_to_pay_from)
"""
class MarketOrder(OrderBase):
    def __init__(self, market_key, qty, payer_acc=None, payee_acc=None):
        OrderBase.__init__(self)
        self.market_key = market_key
        self.qty = qty
        self.payer_acc = payer_acc
        self.payee_acc = payee_acc
        get_global_log().info(str(self)+" of " +str(qty)+ " is created")

    def with_accounts(self, accounts):
        self.payer_acc = accounts[self.market_key.value[1]]
        self.payee_acc = accounts[self.market_key.value[0]]

    def update(self, time, markets):
        OrderBase.update(self, time, markets)

        self.market_price = markets[self.market].get_market_price(time)
        if_price_found = self.market_price is not None

        if if_price_found and not self.is_expired():
            if self.market_key_inverse:
                self.market_price = 1/self.market_price
            # execute the order
            market_value = self.market_price * self.qty
            self.payer_acc.debit(market_value)
            self.payee_acc.credit(self.qty)
            OrderBase.expire(self)  # mark as executed
            get_global_log().info("Order#" + str(self.id) + " is executed: " + self.__str__())


class BuyOrder(MarketOrder):
    def __init__(self, market_key, qty, accounts):
        MarketOrder.__init__(self, market_key, qty, accounts[market_key[1]], accounts[market_key[0]])

class SellOrder(MarketOrder):
    def __init__(self, market_key, qty, accounts):
        MarketOrder.__init__(self, market_key[::-1], qty, accounts[market_key[0]], accounts[market_key[1]])

    def update(self, time, markets):  # has to be overloaded because qty is given in selling equity
        OrderBase.update(self, time, markets)

        self.market_price = markets[self.market].get_market_price(time)
        if_price_found = self.market_price is not None

        if if_price_found and not self.is_expired():
            if not self.market_key_inverse:
                self.market_price = 1/self.market_price
            # execute the order
            market_value = self.market_price * self.qty
            self.payer_acc.debit(self.qty)
            self.payee_acc.credit(market_value)
            OrderBase.expire(self)  # mark as executed
            get_global_log().info("Order#" + str(self.id) + " is executed: " + self.__str__())
