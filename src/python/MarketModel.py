# MarketModel module
import calendar
import requests
import json
from dateutil.parser import parse
from datetime import datetime, timedelta, date


def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

"""
MarketModel base class for modelling a FX market
"""
class MarketModel:
    url = "http://api.fixer.io/" # TODO replace with other source
    data_path = "data/"

    def __init__(self):
        self.baseCurrency = "GBP"
        self.quoteValue = "EUR"  # quote value is not only a currency but also a price e.g. of commodity share
        self.fileName = self.baseCurrency+'.'+self.quoteValue
        self.startDate = parse("2000-01-01")
        self.endDate = datetime.today()
        self.marketprice = {}

    def start_date(self, date_str):
        self.startDate = parse(date_str)

    def end_date(self, date_str):
        self.endDate = parse(date_str)

    def request(self):
        #date_range = daterange(self.startDate, self.endDate) # does not work with fixer- request rate is limited
        date_range = daterange(self.endDate-timedelta(10), self.endDate) # TODO change - avoid fixer.io
        f = open(self.data_path+self.fileName+".csv", 'w')
        f.write("DATE\t" + self.fileName + "\n")
        for d in date_range:
            date_str = '{:%Y-%m-%d}'.format(d)
            req_str = self.url + date_str + "?base=" + self.baseCurrency
            try:
                r = requests.get(req_str)
                f.write(date_str + "\t{}\n".format(r.json()['rates'][self.quoteValue]))
                self.marketprice['{:%Y-%m-%d}'.format(d)] = r.json()['rates'][self.quoteValue]
            except:
                print('Problem with date: ' + req_str)
                raise
        f.close()
        print("saved to file: " + self.fileName)

    def get_market_price(self, timestamp):
        try:
            return self.marketprice[timestamp]
        except:
            pass
        try:
            return self.marketprice['{:%Y-%m-%d}'.format(parse(timestamp))]
        except:
            raise
"""
PerfectModel is the perfect store of market prices
"""
class PerfectFXModel(MarketModel):
    def __init__(self):
        pass

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
    mm.request()
    rate_this_day = mm.get_market_price('2017-07-19')
    print(rate_this_day)
