from marketsim.MarketModel import PerfectFXModel
from marketsim.Constants import CCYMARKET, CCY
from marketsim.Account import Account
from marketsim.Order import Order


"""
Agent base class for various agents with varied strategies for observing and determining markets
"""
class Agent:
    market_models = {}
    def __init__(self, time_keeper, exchange, market_keys, budget_goal):
        self.time = time_keeper
        self.accounts={}
        self.exchange = exchange
        self.budget_goal = budget_goal
        self.strategies=[]
        for k in market_keys:
            self.init_market_model(k, exchange)
            self.init_account(k.value[0])  # base currency account
            self.init_account(k.value[1])  # target currency/equity account

    def init_market_model(self, market_key, exchange):
        if market_key not in self.market_models.keys(): # if not yet added
            if market_key in exchange.markets: # if data is available
                self.market_models[market_key] = exchange.markets[market_key]
            else:
                print("Market requested by an agent does not exist at exchange")
                raise

    def init_account(self, budget_key):
        if budget_key not in self.accounts.keys():
            self.accounts[budget_key] = Account(budget_key)

    def observe(self, market, timestamp):
        too_early = timestamp.current() # usual agent cannot see the future
        if too_early or (market not in self.market_models.keys()):
            return None
        else:
            return self.market_models[market].get_market_price[timestamp]

    def buy(self, market_key, price_in_dest):
        src_acc = self.accounts[market_key.value[0]]
        dst_acc = self.accounts[market_key.value[1]]
        sell_order = BuyOrder(market_key, price_in_dest, src_acc, dst_acc)
        self.exchange.add_order(sell_order)

    def sell(self, market_key, price_in_src):
        src_acc = self.accounts[market_key.value[1]]
        dst_acc = self.accounts[market_key.value[0]]
        buy_order = BuyOrder(market_key, price_in_src, src_acc, dst_acc)
        self.exchange.add_order(buy_order)

    def update(self, time):
        pass

"""
RetroAgent implements Agent that makes decisions based on a perfect model
"""
class RetroAgent(Agent):
    def __str__(self):
        return "***Summary for RetroAgent***\n" + '\n'.join(["{}: {}".format(k, self.accounts[k].balance()) for k in self.accounts.keys()])

    def observe(self, market, timestamp):  # overriding -RetroAgent can see the future
        if market not in self.market_models.keys():
            return None
        else:
            return self.market_models[market].get_market_price[timestamp]

    def update(self, time):
        """
        where a normal agent would observe current market prices and adjust model
        RetroAgent can see the future so....
        populate the model(s) with all observations provided by exchange
        then, if datetime is best buy/sell to maximize budget_goal
        """
        # check if strategies based on current observations places some orders
        new_orders = []
        for strategy in self.strategies:
            new_orders.extend(strategy.execute(self.accounts, self.observe, time))

        # place new orders to exchange
        for order in new_orders:
            self.exchange.add_order(order)


if __name__ == "__main__":
    a = RetroAgent
