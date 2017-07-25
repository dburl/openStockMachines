from enum import Enum
class CCY(Enum):
    EUR=1
    GBP=2
class CCYMARKET(Enum):
    EURGBP=(CCY.EUR,CCY.GBP)

class CCYUtils:
    #TODO this is stupid!!
    def getMarketCCY(market_key):
        if market_key == CCYMARKET.EURGBP:
            return (CCY.EUR,CCY.GBP)
