""""
In the first few steps, you'll have to make sure that the data is in the right format otherwise, Pyfolio will give an error. 
The returns data is available as returns_sp500. 
""""

# Set the index to datetime
returns_sp500.index=pd.to_datetime(returns_sp500.index)

# Ensure the returns are a series
returns=returns_sp500['S&P500']

# Create the returns tear sheet
fig = pf.create_returns_tear_sheet(returns, return_fig=True)

# Display a zoomed in version of the tear sheet
display_tear_sheet()
