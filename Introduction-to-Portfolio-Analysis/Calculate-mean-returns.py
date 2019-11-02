""""

Calculate the percentage returns of the stocks in the DataFrame data by comparing today's price with yesterday's price.
Calculate the mean returns of each stock in the new returns DataFrame.
Assign the weights of the stocks to the weights array. The weights are 0.5, 0.2, 0.2 and 0.1.
Multiply the percentage returns with the weights, and take the total sum, 
to calculate the total portfolio performance and print the results.

""""


# Calculate percentage returns
returns = data.pct_change()

# Calculate individual mean returns 
meanDailyReturns = returns.mean()

# Define weights for the portfolio
weights = np.array([0.5, 0.2, 0.2, 0.1])

# Calculate expected portfolio performance
portReturn = np.sum(meanDailyReturns*weights)

# Print the portfolio return
print(portReturn)
