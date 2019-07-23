'''
Google Finance has deprecated their API but DataReader now makes available the data source 'iex'.
To experiment with the data outside DataCamp environment, you will need an IEX Cloud account.

The most important change to the functionality is the limitation of the data to the last five years.

Retrieving stock price data from IEX is simple after importing the DataReader package and using the start and/or end arguments in form date(YYYY, MM, DD):

stock_data = DataReader(ticker, data_source, start, end)

In the first chapter, you learned that a stock ticker is the unique symbol needed to get stock information for a certain company.

In this exercise, you will practice importing the 2016 data for Apple, with ticker 'AAPL'.
'''

# Import DataReader
from pandas_datareader.data import DataReader

# Import date
from datetime import date

# Set start and end dates
start = date(2016, 1, 1)
end = date(2016, 12, 31)

# Set the ticker
ticker = 'AAPL'

# Set the data source
data_source = 'google'

# Import the stock prices
stock_prices = DataReader(ticker, data_source, start, end)

# Display and inspect the result
print(stock_prices.head())
stock_prices.info()
