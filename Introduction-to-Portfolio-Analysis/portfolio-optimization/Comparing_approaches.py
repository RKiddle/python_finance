""""
In this exercise, you're going to investigate whether the maximum Sharpe portfolios differ when you are using the normal historic expected risk and returns, 
and when using the exponentially weighted risk and returns
""""

# Print the weights of both portfolios types
print(cleaned_weights_maxsharpe, cleaned_weights_maxsharpe_EW, sep="\n")



# Print the performance of both portfolios types
perf_max_sharpe = ef.portfolio_performance(verbose=True)
perf_max_sharpe_EW = ef_2.portfolio_performance(verbose=True)
