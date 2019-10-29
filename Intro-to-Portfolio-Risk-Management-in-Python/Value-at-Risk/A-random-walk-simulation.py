"""
Set the number of simulated days (T) equal to 252, and the initial stock price (S0) equal to 10.
Calculate T random normal values using np.random.normal(), passing in mu and vol, and T as parameters, 
then adding 1 to the values and assign it to rand_rets.
Calculate the random walk by multiplying rand_rets.cumprod() by the initial stock price and assign it to forecasted_values
"""

# Set the simulation parameters
mu = np.mean(StockReturns)
vol = np.std(StockReturns)
T = 252
S0 = 10

# Add one to the random returns
rand_rets = np.random.normal(mu,vol,T) + 1

# Forecasted random walk
forecasted_values = S0*(rand_rets.cumprod())

# Plot the random walk
plt.plot(range(0, T), forecasted_values)
plt.show()
