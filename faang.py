#!/usr/bin/env python3

# Import pandas
import pandas as pd
# Import yfinance package
import yfinance as yf
# Import datetime
import datetime as dt
# Import os
import os
# Import matplotlib
import matplotlib.pyplot as plt
# Import seaborn
import seaborn as sns

# Define function get_data()
# Default parameters for start, end, interval
def get_data(tickers, start = dt.datetime.now() - dt.timedelta(days=5), end = dt.datetime.now(), interval = "1h"):
    # Retrieve historical stock data using yfinance
    data = yf.download(tickers, start=start, end=end, interval=interval, auto_adjust=True)
    # Get current timestamp for filename
    now= dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    # Save data to CSV file in data folder
    data.to_csv("data/" + now + ".csv", sep = ",")

# Call function get_data() with FAANG tickers
get_data(['META', 'AAPL', 'AMZN', 'NFLX' , 'GOOG'])


# Define function plot_data()
def plot_data():
    # Retrieve all csv files in data folder
    list_of_files = os.listdir("data/")
    # Sort files by modification time, newest first
    list_of_files.sort(reverse=True)
    # Get the latest file
    latest_file = list_of_files[0]
    # Import latest file into pandas dataframe (https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
    df = pd.read_csv(f'data/{latest_file}', header=[0, 1], index_col=0, parse_dates=True)
    # Convert index to datetime
    df.index = pd.to_datetime(df.index)

    # Use a modern seaborn theme
    sns.set_theme(style="whitegrid", context="talk", palette="Set1")  # set seaborn theme and color palette

    # Create the plot
    # Set figure size
    plt.figure(figsize=(14, 7))

    # Plot Close prices for each stock
    for ticker in df['Close'].columns:
        plt.plot(df['Close'][ticker], label=ticker)
    # Customize x-axis and rotate labels for better readability
    plt.xticks(rotation=45, fontsize=12)

    # Labels and title
    plt.xlabel('Date', fontsize=14, fontweight='bold')
    plt.ylabel('Close Price (USD)', fontsize=14, fontweight='bold')
    # Title with latest date in data
    plt.title(df.index.max().strftime('%Y-%m-%d'), fontsize=22, pad=20, fontweight='bold')

    # Legend outside plot
    plt.legend(title="Tickers", loc="center left", bbox_to_anchor=(1, 0.5), frameon=True)

    # Improve layout so the legend doesn't get cut off
    plt.tight_layout()

    # Save plot to plots folder
    now = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    plt.savefig("plots/" + now + ".png")

# Call function plot_data()
plot_data()
