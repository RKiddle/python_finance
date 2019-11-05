""""
The DataFrame portfolio_data is available, containing details about the industry classification, obtained from the Global Industry Classification System or "GICS", of your portfolio holdings, 
as well as your portfolio weights and the benchmark weights.
""""

# Print the sum of the bm and pf weights
print (portfolio_data.bm_weights.sum())
print (portfolio_data.pf_weights.sum())

# Group dataframe by GICS sectors 
grouped_df=portfolio_data.groupby('GICS Sector').sum()

# Calculate active weights of portfolio
grouped_df['active_weight']=grouped_df['pf_weights']-grouped_df['bm_weights']
print (grouped_df['active_weight'])
