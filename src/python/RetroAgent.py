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
MarketModel base class for modelling a FX market
"""
class MarketModel:
    def __init__(self):
        pass
    def GetMarketPrice(self,timestamp):
        raise NotImplementedError("GetMarketPrice not implemented yet")
"""
PerfectModel is the perfect store of market prices
"""
class PerfectModel(MarketModel):
    marketprice={}
    def __init__(self):
        pass
    def GetMarketPrice(self,timestamp):
        if timestamp not in marketprice.keys():
            raise ValueError("Requested value not observed yet")
        return marketprice[timestamp]
    def SetMarketPrice(self,timestamp,price):
        marketprice[timestamp] = price
    def SetMarketPrices(self,prices):
        marketprice.update(prices)
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
