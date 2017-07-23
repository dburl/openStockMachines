from enum import Enum
class CCY(Enum):
    EUR=1
    GBP=2
class CCYMARKET(Enum):
    EURGBP=(CCY.EUR,CCY.GBP)
