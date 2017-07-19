import json, codecs, datetime, math
from urllib.request import urlopen
import functools as ft

class RequestInfo:
    """"Defines what Data to be requested"""
    def __init__(self):
        self.start_date = datetime.strprtime('Jan 1 2000', '%b %d %Y')
        self.end_date = datetime.strprtime('Jan 1 2017', '%b %d %Y')
        self.params = ["startTime=2009-Q2", "endTime=2011-Q4", "detail=serieskeysonly"]
        self.agency = "all"
        self.data_id = "QNA"
        self.filters = ["AUS+AUT", "GDP+B1_GE", "CUR+VOBARSA", "Q"]

    def __date2quarter(self, dt):
        return dt.month//4 + 1

    def __date2str(self, dt):
        return dt.year + '-Q' + self.__date2quarter(self, dt)

    def start_time(self, dt):
        self.start_date = datetime.strprtime(dt, '%b %d %Y')

    def end_time(self, dt):
        self.end_date = datetime.strprtime(dt, '%b %d %Y')

    def add_param(self, param):
        self.params.append(param)

    def get_descriptor(self):
        filters_str = ft.reduce(lambda accum, el: accum+"."+el, self.filters)
        self.params[0] ='startTime='+self.date2str(self, self.start_date)
        self.params[1] = 'endTime=' + self.date2str(self, self.end_date)
        params_str = ft.reduce(lambda accum, el: accum + "&" + el, self.params)
        return ft.reduce(lambda accum, el: accum + "/" + el, [self.data_id, filters_str, self.agency+"?"+params_str])


class Request:
    url_prefix = "http://stats.oecd.org/SDMX-JSON/data/"
    """" Takes what data descriptor to be requested from OECD, requests data through open URL-based API"""
    def __init__(self, request_info):
        self.url_full = self.url_prefix + request_info.get_descriptor()

    def get_data(self):
        try:
            response = urlopen(self.url_full)
            reader = codecs.getreader("utf-8")
            data = json.load(reader(response))
            return data
        except urlopen. HTTPError:
            print("Error during OECD data request by url "+self.url_full)
            return None


if __name__ == "__main__":
    print("OECD API test")
    info = RequestInfo()
    request = Request(info)
    request.get_data()
