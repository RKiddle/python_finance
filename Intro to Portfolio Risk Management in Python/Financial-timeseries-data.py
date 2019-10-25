# Import pandas as pd
import pandas as pd

# Read in the csv file and parse dates
StockPrices = pd.read_csv(fpath_csv, parse_dates=['Date'])

# Ensure the prices are sorted by Date
StockPrices = StockPrices.sort_values(by='Date')

# Print only the first five rows of StockPrices
print(StockPrices.head(5))
