
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import seaborn as sns

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

## I like this chart f

y1= a['Adj Close']
fig, ax = plt.subplots(1, 1, figsize=(16,5), dpi= 120)
plt.fill_between(a.index, y1=y1, y2=-y1, alpha=0.5, linewidth=2, color='seagreen')
plt.ylim(-3, 3)
plt.title('Crypto Price (two sided)', fontsize=16)
plt.hlines(y=0, xmin=np.min(a.index), xmax=np.max(a.index), linewidth=.5)
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
dat['year'] = dat.index.year
dat['Month'] = dat.index.month
dat['day'] = dat.index.day


dat.groupby('Month').day_change.mean().plot.bar()


dat.groupby('day').day_change.mean().plot.bar()


# Prepare data
years = dat['year'].unique()

# Draw Plot
fig, axes = plt.subplots(1, 2, figsize=(20,7), dpi= 80)
sns.boxplot(x='year', y='Adj Close', data=dat, ax=axes[0])
sns.boxplot(x='Month', y='Adj Close', data=dat.loc[~dat.year.isin([2020, 2022]), :])

# Set Title
axes[0].set_title('Year-wise Box Plot\n(The Trend)', fontsize=18);
axes[1].set_title('Month-wise Box Plot\n(The Seasonality)', fontsize=18)
plt.show()



## Capture twitter attitudes of currencies
