""""
StockReturns_perc and var_95 from the previous exercise is available in your workspace. Use this data to estimate the VaR for the USO oil ETF for 1 to 100 days from now. 
We've also defined a function plot_var_scale() that plots the VaR for 1 to 100 days from now.
""""

def plot_var_scale():
    # Plot the forecased vs time
    plt.plot(forecasted_values[:,0], -1*forecasted_values[:,1])
    plt.xlabel('Time Horizon T+i')
    plt.ylabel('Forecasted VaR 95 (%)')
    plt.title('VaR 95 Scaled by Time', fontsize=18, fontweight='bold')
    plt.show()
    
# Aggregate forecasted VaR
forecasted_values = np.empty([100, 2])

# Loop through each forecast period
for i in range(0, 100):
    # Save the time horizon i
    forecasted_values[i, 0] = i
    # Save the forecasted VaR 95
    forecasted_values[i, 1] = var_95*np.sqrt(i+1)
    
# Plot the results
plot_var_scale()
