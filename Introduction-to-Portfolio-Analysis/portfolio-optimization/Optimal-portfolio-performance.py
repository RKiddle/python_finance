""""
et's now continue with the efficient frontier ef that you calculated in a previous exercise for the small portfolio. 
You still need to select an optimal portfolio from that efficient frontier ef, and check its performance. Let's use the efficient_return option. This function selects the portfolio with the minimized risk given a target return. A portfolio manager is often asked to manage a portfolio under certain risk and return constraints, so this is a very useful function for that.

mu and Sigma are already calculated for you and ef is also available.
""""

# Get the minimum risk portfolio for a target return 
weights = ef.efficient_return(0.2)
print (weights)

# Show portfolio performance 
ef.portfolio_performance(verbose=True)
