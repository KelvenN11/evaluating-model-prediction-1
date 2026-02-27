import yfinance as yf

def getData():
    ticker_US = yf.Ticker("CL=F")
    ticker_global = yf.Ticker("BZ=F")

    # we create 3 dataset
    # 1. pure US data set
    # 2. pure global data set
    # 3. i% US data set and (100-i)% global data set

    data_US = ticker_US.history(period="10y")
    data_global = ticker_global.history(period="10y")

    # We'll use 80-20 rule for dividing train and test

    split = int(len(data_US) * 0.8)

    data_US_train = data_US[:split]
    data_US_test = data_US[split:]

    data_global_train = data_global[:split]
    data_global_test = data_global[split:]
    
    return data_US_train, data_US_test, data_global_train, data_global_test



