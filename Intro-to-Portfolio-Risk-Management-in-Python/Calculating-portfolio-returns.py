"""
The model portfolio is constructed with pre-defined weights for some of the largest companies in the world just before January 2017:

Company Name	Ticker	Portfolio Weight
Apple	AAPL	12%
Microsoft	MSFT	15%
Exxon Mobil	XOM	8%
Johnson & Johnson	JNJ	5%
JP Morgan	JPM	9%
Amazon	AMZN	10%
General Electric	GE	11%
Facebook	FB	14%
AT&T	T	16%
Note that the portfolio weights should sum to 100% in most cases
"""

# Finish defining the portfolio weights as a numpy array
portfolio_weights = np.array([0.12, 0.15, 0.08, 0.05, 0.09, 0.10, 0.11, 0.14, 0.16])

# Calculate the weighted stock returns
WeightedReturns = StockReturns.mul(portfolio_weights, axis=1)

# Calculate the portfolio returns
StockReturns['Portfolio'] = WeightedReturns.sum(axis=1)

# Plot the cumulative portfolio returns over time
CumulativeReturns = ((1+StockReturns["Portfolio"]).cumprod()-1)
CumulativeReturns.plot()
plt.show()
