# MarketModel module

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