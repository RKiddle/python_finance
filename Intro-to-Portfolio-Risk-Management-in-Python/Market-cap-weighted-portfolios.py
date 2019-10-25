"""

Below is a table of the market capitalizations of the companies in your portfolio just before January 2017:

Company Name	Ticker	Market Cap ($ Billions)
Apple	AAPL	601.51
Microsoft	MSFT	469.25
Exxon Mobil	XOM	349.5
Johnson & Johnson	JNJ	310.48
JP Morgan	JPM	299.77
Amazon	AMZN	356.94
General Electric	GE	268.88
Facebook	FB	331.57
AT&T	T	246.09


"""

# Create an array of market capitalizations (in billions)
market_capitalizations = np.array([601.51, 469.25, 349.5, 310.48, 299.77, 356.94, 268.88, 331.57, 246.09])

# Calculate the market cap weights
mcap_weights = market_capitalizations/sum(market_capitalizations)

# Calculate the market cap weighted portfolio returns
StockReturns['Portfolio_MCap'] = StockReturns.iloc[:, 0:9].mul(mcap_weights, axis=1).sum(axis=1)
cumulative_returns_plot(['Portfolio', 'Portfolio_EW', 'Portfolio_MCap'])
