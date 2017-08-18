from marketsim.MarketModel import PerfectFXModel
from marketsim.Constants import CCYMARKET, CCY
from marketsim.Account import Account
from marketsim.Order import Order

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