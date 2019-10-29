# Historical VaR(90) quantiles
var_90 = np.percentile(StockReturns_perc, 10)
print(var_90)

# Historical CVaR(90) quantiles
cvar_90 = StockReturns_perc[StockReturns_perc<=var_90].mean()
print(cvar_90)

# Plot to compare
plot_hist()
