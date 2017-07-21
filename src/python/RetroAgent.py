from . import MarketModel

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
    def __init__(self, observedtime, buycurrency, sellcurrency, exhangerate):
        Observation.__init__(observedtime)
        self.buyccy = buycurrency
        self.sellccy = sellcurrency
        self.fxrate = fxrate

"""
Agent base class for various agents with varied strategies for observing and determining markets
"""
class Agent:
    def __init__(self):
        pass
    def Observe(self, observation):
        raise NotImplementedError("Observe not implemented yet")
    def Buy(self, ccy, timestamp):
        raise NotImplementedError("Buy not implemented yet")
"""
RetroAgent implements Agent that makes decisions based on a perfect model
"""
class RetroAgent(Agent):
    marketmodels = {}
    holdings = {}
    def __init__(self, market, ccy):
        Agent.__init__(self)
        StartModelling(market)
        StartHolding(ccy)
    def StartModelling(self,market):
        model[market] = PerfectModel
    def StartHolding(self,market):
        model[market] = 0
    def Observe(self, fxobservation):
        if fxobservation.market not in marketmodel.keys():
            StartModelling(market)
        model[fxobservation.market].SetMarketPrice(fxobservation.timestamp,fxobservation.fxrate)
    def Recieve(self, ccy, qty):
        if ccy not in holdings.keys():
            StartHolding(ccy)
        holdings[ccy] += qty
    def Buy(self, ccy, timestamp):
        raise NotImplementedError("TODO: Buy impl using previous fx observations")



if __name__ == "__main__":
    a = RetroAgent
    #a.run() #TODO
