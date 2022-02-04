
import pandas as pd


#!pip install yfinance
import yfinance as yf
import datetime as dt

start = dt.datetime(2020,1,1)
end = dt.datetime.now()

eth = yf.download('ETH', start, end)
eth
