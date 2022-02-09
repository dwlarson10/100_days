
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

from crypto_function import *


crypt = ['ADA-USD']

dat = pd.DataFrame()

for c in crypt:
    tmp = crypto_function(c)
    tmp['currency'] = c
    tmp['day_change'] = tmp['Close'] - tmp['Open']
    dat = dat.append(tmp)


dat.head()

dat.groupby('currency').max()

# Starting to build timeseries data

# Playing around with some basic charts in matplotlib

a = dat
plt.plot(a.index, a['Adj Close'], label='Daily Adj Close Price')
plt.title('ADA Past 12 Months')
plt.legend(loc='best')
plt.ylabel('Price ($)');
plt.show()

a = dat
plt.plot(a.index, a['day_change'], label='Daily Change')
plt.plot(a['day_change'].rolling(30).mean(),label= 'MA 30 days')
plt.title('ADA Past 12 Months')
plt.legend(loc='best')
plt.ylabel('Price ($)');
plt.show()

#plt.plot(a['Adj Close'].rolling(14).mean(),label= 'MA 14 days')
#plt.plot(a['Adj Close'].rolling(30).mean(),label= 'MA 30 days')
#plt.plot(a['Adj Close'].rolling(90).mean(),label= 'MA 90 days')



## Data to build


# Extracting the year, month

dat['Month'] = dat.index.month
dat['day'] = dat.index.day


dat.groupby('Month').day_change.mean().plot.bar()


dat.groupby('day').day_change.mean().plot.bar()

## Capture twitter attitudes of currencies
