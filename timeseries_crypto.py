
import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
import seaborn as sns
import plotly.express as px


st.title('Learning timeseries with Cryptocurrencies')



a = st.sidebar.text_input('Enter a CrytoCurrency')
st.sidebar.text('Examples: \n ADA-USD = Cardona \n BTC-USD = Bitcoid')


@st.cache
def crypto_function(crypto):
    import pandas as pd
    import yfinance as yf
    import datetime as dt

    start = dt.datetime.now() - dt.timedelta(days = 365*2)
    end = dt.datetime.now()
    tmp = yf.download(crypto, start, end)
    ## Adding Moving Averages to the dataset
    #tmp = pd.DataFrame(tmp)
    ##tmp['MA_14_day'] = tmp['Close'].rolling(14).mean(),label= 'MA 14 days')
    #tmp['MA_30_day'] = tmp['Close'].rolling(30).mean(),label= 'MA 14 days')
    #tmp['MA_60_day'] = tmp['Close'].rolling(60).mean(),label= 'MA 14 days')
    #tmp['MA_90_day'] = tmp['Close'].rolling(90).mean(),label= 'MA 14 days')

    #tmp['day_change'] = tmp['Close'] - tmp['Open']


    return(tmp)

crypt = [a]

data_load_state = st.text('Loading data...')
dat = crypto_function(crypt)
dat2 = dat

dat2['MA 14'] = dat2['Close'].rolling(14).mean()
#plt.plot(a['Adj Close'].rolling(30).mean(),label= 'MA 30 days')
#plt.plot(a['Adj Close'].rolling(90).mean(),label= 'MA 90 days')


data_load_state.text('Loading data...done!')


col1, col2 = st.columns(2)

col2.subheader('Raw data')
col2.write(dat2)

col1.subheader('Trending data')
col1.line_chart(dat.Close)

fig = px.line(dat2)
col1.plotly_chart(fig)
