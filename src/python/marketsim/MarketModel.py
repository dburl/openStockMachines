# MarketModel module
import calendar
import requests, os, sys
import json
from dateutil.parser import parse
from datetime import datetime, timedelta, date
import matplotlib.pyplot as plt
import quandl, tokens
import pandas as pd
from marketsim.Constants import CCYMARKET, CCY
from pathlib import Path

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

"""
MarketModel base class for modelling a FX market
"""
class MarketModel:
    data_path = "data/"

    def __init__(self, requested_market=None):
        self.startDate = parse("2000-01-01")
        self.endDate = datetime.today()
        self.marketprice = {}
        self.market_key = None
        self.df = None
        if requested_market is not None:
            self.set_market(requested_market)

    def set_market(self, requested_market):
        self.market_key = requested_market
        if type(self.market_key) == CCYMARKET:
            self.get_quandl_data()

    def __str__(self):
        return self.base_currency_name() + '-' + self.quote_value_name()

    def base_currency_name(self):  #e.g. USD/EUR/etc
        if type(self.market_key) == CCYMARKET:
            if type(self.market_key) == CCYMARKET:
                return self.market_key.value[0].name
        else:
            print("Unexpected market data request")
            raise

    def quote_value_name(self):  #e.g. GOLD/OIL/GOOGLE/etc
        if type(self.market_key) == CCYMARKET:
            if type(self.market_key) == CCYMARKET:
                return self.market_key.value[1].name
        else:
            print("Unexpected market data request")
            raise

    def get_quandl_data(self):
        agency = 'ECB'
        file_name = self.data_path + self.__str__() + ".csv"
        data_file = Path(file_name)
        if data_file.is_file():
            self.df = pd.read_csv(file_name, sep='\t', index_col=0)
            print("read from file: " + file_name)
        else:
            self.df = quandl.get(agency+'/'+self.base_currency_name()+self.quote_value_name(), authtoken=tokens.get_quandl_tocken())
            if not os.path.exists(self.data_path):
                os.makedirs(self.data_path)
            #self.df.to_csv(file_name, index=True, sep='\t')
            self.df.to_csv(file_name, sep='\t',  index=False, index_col=False)
            print("saved to file: " + file_name)

    def start_date(self, date_str):
        self.startDate = parse(date_str)

    def end_date(self, date_str):
        self.endDate = parse(date_str)

    def get_market_price(self, timestamp):
        try:
            return self.df.loc[timestamp].values[0]
        except:
            pass
        try:
            date = timestamp.strftime("%Y-%m-%d")
            return self.df.ix[date].values[0]
        except:
            return None
"""
PerfectModel is the perfect store of market prices
"""
class PerfectFXModel(MarketModel):

    def get_market_price(self, timestamp):
        if timestamp not in self.marketprice.keys():
            raise ValueError("Requested value not observed yet")
        return self.marketprice[timestamp]

    def set_market_price(self, timestamp, price):
        self.marketprice[timestamp] = price

    def set_market_prices(self, prices):
        self.marketprice.update(prices)


if __name__ == "__main__":
    print("Market Model test")
    mm = MarketModel()
    mm.collect_market_data()
    rate_this_day = mm.get_market_price('2017-07-19')
    print(rate_this_day)
