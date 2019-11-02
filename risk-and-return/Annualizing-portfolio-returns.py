"""
So let's calculate the annualized rate of return for your portfolio. 

Since our sample covers 3.2 years, let's use the monthly denomination in the formula for annualized returns. 
The number of months is already given under months.

Available are the data on portfolio returns under pf_returns, 
as well as as a separate series pf_AUM containing the portfolio's value, or assets under management (AUM). 
""""

# Calculate total rate of return from start to end
total_return = (pf_AUM[-1] - pf_AUM[0]) / pf_AUM[0]

# Annualize return
annualized_return = ((1 + total_return)**(12/months))-1
print (annualized_return)
