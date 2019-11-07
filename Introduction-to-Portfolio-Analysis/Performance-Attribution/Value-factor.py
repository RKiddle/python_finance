""""
Let's now check how our portfolio measures up to this, 
and let's especially focus on value. Available to you is a DataFrame called factor_data containing 
the factor returns as well as your portfolio returns. Start by inspecting the DataFrame factor_data 
in the IPython shell using factor_data.head().
""""

# Calculate the pairwise correlation
factor_data.corr()

# Calculate rolling 5 day correlation 
factor_data['correlation_value']=factor_data['portfolio'].rolling(5).corr(factor_data['value'])

# Plot the rolling correlation
factor_data['correlation_value'].plot()
plt.legend()
plt.show()
