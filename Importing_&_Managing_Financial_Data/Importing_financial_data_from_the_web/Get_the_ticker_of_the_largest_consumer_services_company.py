# Set the index of listings to Stock Symbol
listings = listings.set_index('Stock Symbol')

# Get ticker of the largest Consumer Services company
ticker = listings.loc[listings.Sector == 'Consumer Services', 'Market Capitalization'].idxmax()

# Set the start date
start = date(2012, 1, 1)

# Import the stock data
data = DataReader(ticker, 'google', start)

# Plot Close and Volume
data[['Close', 'Volume']].plot(secondary_y='Volume', title=ticker)

# Show the plot
plt.show()
