""""
Available is portfolio data containing weights and asset returns under portfolio_data. 
Have a look at the data by running portfolio_data.head(10) in the IPython Shell. 
""""

# Check the portfolio weights
print(portfolio_data.pf_weights.sum())

# Calculate return of the portfolio
total_return_pf = (portfolio_data['pf_weights']*portfolio_data['mean_return']).sum()

# Calculate return of the benchmark
total_return_bm = (portfolio_data['bm_weights']*portfolio_data['mean_return']).sum()

# Calculate and print the active return
active_return = total_return_pf - total_return_bm
print ("%.2f%%" % active_return)
