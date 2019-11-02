""""
The value of the S&P500 between 1st of January 2015 and end of December 2018 has been made available. 
That's 4 years of data. You have full years this time,
so use the year denomination in the formula for the annualized return. 
The data is stored under sp500_value
""""

# Calculate the total return from the S&P500 value series
total_return = (sp500_value[-1] - sp500_value[0]) / sp500_value[0]
print(total_return)

# Annualize the total return spanning 4 years
annualized_return = ((1 + total_return)**(1/4))-1
print (annualized_return)
