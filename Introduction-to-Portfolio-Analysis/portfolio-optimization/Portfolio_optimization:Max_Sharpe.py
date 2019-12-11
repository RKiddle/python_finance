""""
PyPortfolioOpt makes it very easy to calculate this portfolio from a set of historical price data.

Available for you are the mean historic return 
for a small portfolio of stocks under mu and a covariance matrix belonging to our portfolio under Sigma.
""""

# Define the efficient frontier
ef = EfficientFrontier(mu, Sigma)

# Calculate weights for the maximum Sharpe ratio portfolio
raw_weights_maxsharpe = ef.max_sharpe()
cleaned_weights_maxsharpe = ef.clean_weights()
print (raw_weights_maxsharpe, cleaned_weights_maxsharpe)
