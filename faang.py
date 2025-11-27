#!/usr/bin/env python3

#import pandas
import pandas as pd
#import yfinance package
import yfinance as yf
#import datetime
import datetime as dt
#import os
import os
# import matplotlib
import matplotlib.pyplot as plt
#import seaborn
import seaborn as sns

# define function get_data()
def get_data(tickers, start = dt.datetime.now() - dt.timedelta(days=5), end = dt.datetime.now(), interval = "1h"):
    data = yf.download(tickers, start=start, end=end, interval=interval, auto_adjust=True)
    now= dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    data.to_csv("data/" + now + ".csv", sep = ",")

# call function get_data() with FAANG tickers
get_data(['META', 'AAPL', 'AMZN', 'NFLX' , 'GOOG'])

#retrieve all csv files in data folder
list_of_files =os.listdir("data/")
print(list_of_files)

#sort files by modification time
list_of_files.sort(reverse = True)

latest_file = list_of_files[0]

#import latest file into pandas dataframe
df = pd.read_csv(f'data/{latest_file}', header=[0,1], index_col=0, parse_dates=True)

# convert index to datetime
df.index = pd.to_datetime(df.index)

# plot close prices of each stock
sns.set_theme(style="whitegrid", context="talk", palette="Set1") #set seaborn theme and color palette (https://www.practicalpythonfordatascience.com/ap_seaborn_palette)
plt.figure(figsize=(14, 7)) # Set figure size
for ticker in df['Close'].columns:
    plt.plot(df['Close'][ticker], label=ticker) # Plot each stock's close price
plt.xticks(rotation=45, fontsize=12) # Rotate x-axis labels for better readability
# Labels and title
plt.xlabel('Date', fontsize=14, fontweight='bold')
plt.ylabel('Close Price (USD)', fontsize=14, fontweight='bold')
plt.title('Close Prices of FAANG Stocks', fontsize=22, pad=20, fontweight='bold')
# Legend outside plot
plt.legend(title="Tickers", loc="center left", bbox_to_anchor=(1, 0.5), frameon=True)
# Improve layout so the legend doesn't get cut off
plt.tight_layout()
#save plot to plots folder
now= dt.datetime.now().strftime("%Y%m%d-%H%M%S")
plt.savefig("plots/" + now + ".png")
plt.show()



