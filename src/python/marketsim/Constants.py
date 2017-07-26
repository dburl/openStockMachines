from enum import Enum
class CCY(Enum):
    USD=1
    INR=2
    EUR=3
    GBP=4
class CCYMARKET(Enum):
    EURGBP=(CCY.EUR,CCY.GBP)
    USDINR=(CCY.USD,CCY.INR)
