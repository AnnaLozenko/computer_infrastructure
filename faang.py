#!/usr/bin/env python3

#import pandas
import pandas as pd
#import yfinance package
import yfinance as yf
#import datetime
import datetime as dt
#import glob
import glob
#import os
import os
# import matplotlib
import matplotlib.pyplot as plt

# define function get_data()
def get_data(tickers, start = dt.datetime.now() - dt.timedelta(days=5), end = dt.datetime.now(), interval = "1h"):
    data = yf.download(tickers, start=start, end=end, interval=interval, auto_adjust=True)
    now= dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    data.to_csv("data/" + now + ".csv", sep = ",")

# call function get_data() with FAANG tickers
get_data(['META', 'AAPL', 'AMZN', 'NFLX' , 'GOOG'])

#retrieve all csv files in data folder
list_of_files =glob.glob("data/*.csv")

#sort files by modification time
latest_file = max(list_of_files, key=os.path.getmtime)

#import latest file into pandas dataframe
df = pd.read_csv(latest_file, header=[0,1], index_col=0, parse_dates=True)

# convert index to datetime
df.index = pd.to_datetime(df.index)

# plot close prices of each stock
plt.figure(figsize=(12,6))
for ticker in df['Close'].columns:
    plt.plot(df['Close'][ticker], label=ticker)
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('Close Prices of FAANG Stocks')
plt.legend()
#save plot to plots folder
now= dt.datetime.now().strftime("%Y%m%d-%H%M%S")
plt.savefig("plots/" + now + ".png")


