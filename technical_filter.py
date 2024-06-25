import yfinance as yf
import pandas as pd
from ta.momentum import RSIIndicator
def p_eratio(symbol):
    data=yf.Ticker(symbol)
    main=data.info
    earning_per_share=main.get('trailingPE')
    closing_price=main.get('previousClose')
    if(earning_per_share is not None and closing_price is not None):
        p_e=closing_price/earning_per_share
        return p_e
    else:
        return -1
def average_price(symbol):
    data=yf.download(symbol,period='365d',interval='1d')
    average=0
    for i in range(len(data)):
        average=average+data["Close"][i]
    average=average/len(data)
    return average
def rsi(symbol):
    data=yf.download(symbol,period='365d',interval='1d')
    calculation=14
    rsi = RSIIndicator(data["Close"], window=calculation)
    rsi_value=rsi.rsi()
    return rsi_value[len(rsi_value)-1]
def average_volume(symbol):
    data=yf.download(symbol,period='365d',interval='1d')
    average=0
    for i in range(len(data)):
        average=average+data["Volume"][i]
    average=average/len(data)
    return average
def closing_price(symbol):
    data=yf.download(symbol,period='365d',interval='1d')
    return data['Close'][len(data)-1]

def technical_filter_function(technical_filter):
    technical_filter_dict={}
    file_path = 'Nifty50.csv'
    df = pd.read_csv(file_path)
    mylist=(df["Symbol"])
    for i in range(len(mylist)):
        symbol=mylist[i]+".NS"
        if(technical_filter=="Price to Earning ratio"):
            technical_filter_value=p_eratio(symbol)
        if(technical_filter=="Average price"):
            technical_filter_value=average_price(symbol)
        if(technical_filter=="Relative Strength Index"):
            technical_filter_value=rsi(symbol)
        if(technical_filter=="Average volume"):
            technical_filter_value=average_volume(symbol)
        if(technical_filter=="Recent closing price"):
            technical_filter_value=closing_price(symbol)
        if(technical_filter_value!=-1):
            technical_filter_dict[mylist[i]]=technical_filter_value
    return technical_filter_dict
