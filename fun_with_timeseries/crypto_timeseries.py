
import pandas as pd
import matplotlib.pyplot as plt

from crypto_function import *


crypt = ['BTC-USD','ETH-USD','ADA-USD']

dat = pd.DataFrame()

for c in crypt:
    tmp = crypto_function(c)
    tmp['currency'] = c
    dat = dat.append(tmp)


dat.head()

dat.groupby('currency').max()

# Starting to build timeseries data

# Playing around with some basic charts in matplotlib

t = dat[dat['currency'] == 'BTC-USD']
plt.plot(t.index, t['Adj Close'])
plt.title('BTC Past 12 Months')
plt.ylabel('Price ($)');
plt.show()

a = dat[dat['currency'] == 'ETH-USD']
plt.plot(a.index, a['Adj Close'])
plt.plot(a['Adj Close'].rolling(14).mean(),label= 'MA 14 days')
plt.plot(a['Adj Close'].rolling(30).mean(),label= 'MA 30 days')
plt.plot(a['Adj Close'].rolling(90).mean(),label= 'MA 90 days')
plt.title('ETH Past 12 Months')
plt.legend(loc='best')
plt.ylabel('Price ($)');
plt.show()




## Data to build

## Capture twitter attitudes of currencies
