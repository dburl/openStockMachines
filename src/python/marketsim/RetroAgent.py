from marketsim.MarketModel import PerfectFXModel
from marketsim.Constants import CCYMARKET, CCY
from marketsim.Exchange import Account

"""
Observation base class for various market specific observation sub classes
"""
class Observation:
    def __init__(self, observedtime):
        self.timestamp = observedtime
"""
FXObservation sub class records an exchange rate at single pt in time between currencies
"""
class FXObservation(Observation):
    def __init__(self, observedtime, buycurrency, sellcurrency, fxrate):
        Observation.__init__(observedtime)
        self.buyccy = buycurrency
        self.sellccy = sellcurrency
        self.fxrate = fxrate

"""
Agent base class for various agents with varied strategies for observing and determining markets
"""
class Agent:

    def __init__(self, markets={}, budget={}):
        self.budget = budget  # initial money/currency pairs/equities an agent possesses
        self.markets = markets  # markets/environments an agent is aware about and can trade on them

    def Observe(self, observation):
        raise NotImplementedError("Observe not implemented yet")

    def Buy(self, budget_key, budget_amount, timestamp):
        raise NotImplementedError("Buy not implemented yet")

    def Sell(self, budget_key, budget_amount, timestamp):
        raise NotImplementedError("Buy not implemented yet")
"""
RetroAgent implements Agent that makes decisions based on a perfect model
"""
class RetroAgent(Agent):
    models = {}
    def __init__(self, exchange, market_keys, budget_goal):
        Agent.__init__(self)
        self.exchange = exchange
        self.budget_goal = budget_goal
        for k in market_keys:
            self.init_model(k)
            self.init_budget(k[0])
            self.init_budget(k[1])
    def init_model(self,market_key):
        if market_key not in self.models.keys():
            self.models[market_key] = PerfectFXModel
    def init_budget(self,budget_key):
        if budget_key not in self.budget.keys():
            self.budget[budget_key] = Account(budget_key)
    def Observe(self, fxobservation):
        if fxobservation.market not in models.keys():
            init_model(fxobservation.market)
        models[fxobservation.market].SetMarketPrice(fxobservation.timestamp,fxobservation.fxrate)
    def Buy(self, market_key):
        full_balance = self.budget[market_key[0]]
        src_acc = self.budget[market_key[0]]
        dst_acc = self.budget[market_key[1]]
        buy_order = BuyOrder(market_key, full_balance, src_acc, dst_acc)
        self.exchange.add_order(buy_order)
    def update(self):
        """
        where a normal agent would observe current market prices and adjust model
        RetroAgent can see the future so....
        populate the model(s) with all observations provided by exchange
        then, if datetime is best buy/sell to maximize budget_goal
        """
        raise NotImplementedError("TODO: act upon strategy using market model")


if __name__ == "__main__":
    a = RetroAgent
