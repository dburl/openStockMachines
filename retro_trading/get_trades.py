import numpy as np

ratesFile = "exchange_rates.csv"


rates = np.genfromtxt(ratesFile,skip_header=1,usecols=1,delimiter=',')
future_best = rates[-1]
results = []

for rate in np.flip(rates,0):
    execute = rate >= future_best
    results.insert(0,execute)
    future_best = max(future_best,rate)

print(results)
