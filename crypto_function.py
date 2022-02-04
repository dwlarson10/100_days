



def crypto_function(crypto):
    import pandas as pd
    import yfinance as yf
    import datetime as dt

    start = dt.datetime(2021,1,1)
    end = dt.datetime.now()

    tmp = yf.download(crypto, start, end)
    return(tmp)
