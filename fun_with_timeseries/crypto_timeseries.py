# Loading Packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import seaborn as sns
import plotly.express as px
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.tsa.stattools import acf

#User Developed functions
from crypto_function import *

n_steps = 2
def rolling_difference(x):
    return x.iloc[-1] - x.iloc[0]


## Data Wrangling
crypt = ['BTC-USD']

dat = pd.DataFrame()

for c in crypt:
    tmp = crypto_function(c)
    tmp['currency'] = c
    tmp['day_change'] = tmp['Close'] - tmp['Open']
    tmp['year'] = tmp.index.year
    tmp['Month'] = tmp.index.month
    tmp['day'] = tmp.index.day

    # Moving Averages
    tmp['14_d_ma'] = tmp['Close'].rolling(14).mean()
    tmp['90_d_ma'] = tmp['Close'].rolling(90).mean()
    tmp['200_d_ma'] = tmp['Close'].rolling(200).mean()
    tmp['rolling_volume_difference'] = tmp['Volume'].rolling(window=n_steps).apply(rolling_difference)
    dat = dat.append(tmp)




dat.groupby('currency').max()

# Starting to build timeseries data

# Playing around with some basic charts in matplotlib

a = dat[['Close','14_d_ma','90_d_ma','200_d_ma']]
plt.plot(a,label=['Daily Close Price','14 Day Moving Average','90 Day Moving Average','200 Day Moving Average'])
plt.title('Trending')
plt.legend(loc='best')
plt.ylabel('Price ($)')
plt.show()

## I like this chart f
peak_price = max(a['Close'])
y1= a['Close']
fig, ax = plt.subplots(1, 1, figsize=(16,5), dpi= 120)
plt.fill_between(a.index, y1=y1, y2=-y1, alpha=0.5, linewidth=2, color='seagreen')
plt.ylim(-peak_price, peak_price)
plt.title('Crypto Price (two sided)', fontsize=16)
plt.hlines(y=0, xmin=np.min(a.index), xmax=np.max(a.index), linewidth=.5)
plt.show()



plt.plot(dat.index, dat['day_change'], label='Daily Change')
plt.plot(dat['day_change'].rolling(30).mean(),label= 'MA 30 days')
plt.title('ADA Past 12 Months')
plt.legend(loc='best')
plt.ylabel('Price ($)')

plt.show()


dat.groupby('Month').day_change.mean().plot.bar()


dat.groupby('day').day_change.mean().plot.bar()


# Prepare data
years = dat['year'].unique()

# Draw Plot
fig, axes = plt.subplots(1, 2, figsize=(20,7), dpi= 80)
sns.boxplot(x='year', y='Close', data=dat, ax=axes[0])
sns.boxplot(x='Month', y='Close', data=dat.loc[~dat.year.isin([2020, 2022]), :])
axes[0].set_title('Year-wise Box Plot\n(The Trend)', fontsize=18);
axes[1].set_title('Month-wise Box Plot\n(The Seasonality)', fontsize=18)
plt.show()
## Timeseries Models
# Types of timeseries models to building

#Moving Average
# ARIMA


##

dat_model = pd.DataFrame(dat['Close'])

dat_model.reset_index(inplace=True)
dat_model = dat_model.rename(columns = {'index':'Date'})


dat_model = dat_model.set_index('Date')

dat_model

random_walk_acf_coef = acf(dat_model)
plot_acf(dat_model, lags=20);

random_walk_diff = np.diff(dat_model.Close)

print(random_walk_diff)

plt.figure(figsize=[10, 7.5]); # Set dimensions for figure
plt.plot(random_walk_diff)
plt.title('Noise')
plt.show()


plot_acf(random_walk_diff, lags=20);

## Moving Average

ar2 = np.array([2])
ma2 = np.array([1, 0.9, 0.3])

MA2_process = ArmaProcess(ar2, ma2).generate_sample(nsample=1000)
