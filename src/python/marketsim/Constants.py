from enum import Enum
class CCY(Enum):
    USD = 1
    INR = 2
    EUR = 3
    GBP = 4
class CCYMARKET(Enum):
    EURGBP = (CCY.EUR, CCY.GBP)  # GBP per 1 EUR
    EURUSD = (CCY.EUR, CCY.USD)  # USD per 1 EUR
    USDINR = (CCY.USD, CCY.INR)  # INR per 1 USD

