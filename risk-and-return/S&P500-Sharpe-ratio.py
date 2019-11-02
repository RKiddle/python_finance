""""
In this exercise, you're going to calculate the Sharpe ratio of the S&P500, starting with pricing data only. 
In the next exercise, you'll do the same for the portfolio data, such that you can compare the Sharpe ratios of the two.

Available for you is the price data from the S&P500 under sp500_value. 
The risk-free rate is available under rfr, which is conveniently set to zero. Let's give it a try!
"""

# Calculate total return and annualized return from price data 
total_return = (sp500_value[-1] - sp500_value[0]) / sp500_value[0]

# Annualize the total return over 4 year 
annualized_return = ((1 + total_return)**(1/4))-1

# Create the returns data 
returns_sp500 = sp500_value.pct_change()

# Calculate annualized volatility from the standard deviation
vol_sp500 = returns_sp500.std() * np.sqrt(250)

# Calculate the Sharpe ratio 
sharpe_ratio = ((annualized_return - rfr) / vol_sp500)
print (sharpe_ratio)
