# FAANG Stock Data Analysis and Automation

This repository demonstrates a complete automated workflow for retrieving, processing, and visualising FAANG stock data using Python. The project combines data acquisition, processing, visualisation, scripting, and cloud-based automation to create a reproducible data pipeline.

The project was created as part of Computer Infrastructure assessment and includes the solution to the following tasks:

1. Data retrieval using the yfinance package
2. Data visualisation
3. Executable script
4. Automation with GitHub Actions

The repository contains the following key components:

- A Python script ([faang.py](https://github.com/AnnaLozenko/computer_infrastructure/blob/main/faang.py)) that downloads the latest hourly prices for FAANG stocks and generates a plot.

- A Jupyter notebook ([problems.ipynb](https://github.com/AnnaLozenko/computer_infrastructure/blob/main/problems.ipynb)) with explanations of the code, steps taken, and workflow description.

- A [data](https://github.com/AnnaLozenko/computer_infrastructure/tree/main/data) folder storing downloaded CSV files.

- A [plots](https://github.com/AnnaLozenko/computer_infrastructure/tree/main/plots) folder storing generated PNG plots.

- A GitHub Actions workflow ([faang.yml](https://github.com/AnnaLozenko/computer_infrastructure/blob/main/.github/workflows/faang.yml)) that runs the script automatically every Saturday morning.

- A [requirements.txt](https://github.com/AnnaLozenko/computer_infrastructure/blob/main/requirements.txt) file listing the necessary Python packages.

- A gitignore file to exclude unnecessary files from the repository.

**Repository Structure**
```
├── faang.py                 # Main executable script
├── notebook.ipynb           # Same code as script + explanations
├── data/                    # CSV files downloaded using yfinance
├── plots/                   # Saved plot images (PNG files)
├── requirements.txt         # Required Python packages
├── .gitignore               
└── .github/                 
    └── workflows/
        └── faang.yml        # GitHub Actions workflow (automation)
```

## Overview
This project retrieves hourly stock price data for the last 5 days using the [yfinance](https://ranaroussi.github.io/yfinance/) package for the following FAANG companies:

-META (Meta, formerly Facebook)

-AAPL (Apple)

-AMZN (Amazon)

-NFLX (Netflix)

-GOOG (Alphabet, formerly Google)

The script processes and visualizes the Close prices on a single plot, then saves both the CSV data and PNG plot using timestamped filenames.
A GitHub Actions workflow (`faang.yml`) is included to run the script automatically every Saturday morning at 9:00 AM UTC.

## Data Downloading - ```get_data()```

The script defines a function
```get_data(tickers, start, end, interval)``` that takes a list of stock tickers, start and end dates, and data interval as input parameters. It uses the yfinance library to download historical stock data for each ticker within the specified date range and interval. The downloaded data is saved as CSV files in the `data/` folder with filenames that include the ticker symbol and timestamp (```YYYYMMDD-HHmmss.csv```)

## Plotting - ```plot_data()```

The script also defines a function `plot_data()` that reads the most recent CSV file from the `data/` folder, extracts the Close prices, and generates a line plot showing the stock prices over time for all FAANG companies. The plot is saved as a PNG file in the `plots/` folder with a timestamped filename (`YYYYMMDD-HHmmss.png`).  

## Automation with GitHub Actions

A GitHub Actions workflow (`faang.yml`) is set up to automate the execution of the script. The workflow is scheduled to run every Saturday at 9:00 AM UTC. When triggered, it checks out the repository, sets up Python, installs the required packages from `requirements.txt`, and runs the `faang.py` script to download the latest stock data and generate the plot. All individual lines of the workflow are explained in detail in the notebook.  

## Requirements

The project requires the following Python packages, which are listed in the `requirements.txt` file:
- yfinance
- pandas
- matplotlib
- seaborn

To install the required packages, run:
```
pip install -r requirements.txt
```

or install them manually using pip:
```
pip install yfinance pandas matplotlib seaborn
```

## Usage

### Manual Execution
To run the script manually, execute the following command in your terminal:
``` 
python faang.py
```
This will download the latest FAANG stock data, generate the plot, and save the files in the respective folders. If the `data/` and `plots/` folders do not exist, they must be created beforehand.

### Automated Execution

The GitHub Actions workflow will automatically execute the script every Saturday at 9:00 AM UTC.  

## Jupyter Notebook
The [problems.ipynb]() notebook contains the same code as in the `faang.py` script, along with detailed explanations of each step, the workflow description, and insights into the data pipeline process. 



