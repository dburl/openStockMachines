import calendar
import requests
import json

ratesFile = "exchange_rates.csv"
url = "http://api.fixer.io/"
srcCurrency = "GBP"
dstCurrency = "EUR"

f = open(ratesFile,'w')
f.write("DATE,"+srcCurrency+dstCurrency+"\n")
for m in range(1,13):
	dateStr = "2016-{:02d}-{}".format(m,calendar.monthrange(2016,m)[1])
	reqStr = url + dateStr + "?base=" + srcCurrency
	r = requests.get(reqStr)
	f.write(dateStr+",{}\n".format(r.json()['rates'][dstCurrency]))

f.close()
print("saved to file: "+ratesFile)
