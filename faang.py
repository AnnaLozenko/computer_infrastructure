#!/usr/bin/env python3

# pandas is a powerful data analysis and manipulation library for Python.
import pandas as pd
# yfinance is set of tools to download market data from Yahoo Finance.
import yfinance as yf
# datetime module supplies classes for manipulating dates and times.
import datetime as dt
# os module provides a way of using operating system dependent functionality.
import os
# matplotlib is a comprehensive library for creating visualizations in Python.
import matplotlib.pyplot as plt
# seaborn is a Python data visualization library based on matplotlib
import seaborn as sns

def get_data(tickers, start = dt.datetime.now() - dt.timedelta(days=5), end = dt.datetime.now(), interval = "1h"):
    """
    Download historical market data for the given tickers and save to CSV.
    The CSV file is saved in the 'data' folder with a timestamped filename.

    :param tickers: List containing one or more ticker symbols supported by yfinance.
    :param start: Start datetime for the historical data. Defaults to 5 days ago.
    :param end: End datetime for the historical data. Defaults to now.
    :param interval: Data sampling interval (e.g. '1m', '1h', '1d'). Defaults to '1h'.
    :return: None.
    """
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
    """
    Load the latest CSV file from the 'data' folder, plot the Close prices for each stock.
    Save the plot to the 'plots' folder with a timestamped filename.
    :return: None
    """
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
