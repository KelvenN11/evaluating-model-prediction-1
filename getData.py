import yfinance as yf
import numpy as np

def getData():
    ticker_US = yf.Ticker("CL=F")
    ticker_global = yf.Ticker("BZ=F")

    data_US = ticker_US.history(period="10y")
    data_global = ticker_global.history(period="10y")
    
    data_US, data_global = data_US.align(data_global, join='inner', axis=0)
    valid_mask = (data_US["Close"] > 0) & (data_global["Close"] > 0)

    # We only want close price
    data_US = data_US[valid_mask]
    data_global = data_global[valid_mask]
    
    data_US = np.array(data_US["Close"])
    data_global = np.array(data_global["Close"])
    
    # find the log
    data_US = np.log(data_US[1:] / data_US[:-1])
    data_global = np.log(data_global[1:] / data_global[:-1])
    
    data_US = data_US[~np.isnan(data_US)]
    data_global = data_global[~np.isnan(data_global)]
    
    window = 5
    
    data_US_train = []
    data_US_test = []
    data_global_train = []
    data_global_test = []
    
    for t in range(window, len(data_US)-1):
        data_US_train.append(data_US[t-window:t])
        data_US_test.append(data_US[t])
        
    for t in range(window, len(data_global)-1):
        data_global_train.append(data_global[t-window:t])
        data_global_test.append(data_global[t])
    
    return data_US_train, data_US_test, data_global_train, data_global_test



