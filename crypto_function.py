



def crypto_function(crypto,days=1000):
    import pandas as pd
    import yfinance as yf
    import datetime as dt

    start = dt.datetime.now() - dt.timedelta(days = - days)
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
