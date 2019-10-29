""""

You can call the .fit() method from statsmodels.formula.api on an .ols(formula, data) 
model object to perform the analysis, and the .summary() method on the analysis object to anaylze the results.

The FamaFrenchData DataFrame is available in your workspace and contains the proper data for this exercise.

""""

# Import statsmodels.formula.api
import statsmodels.formula.api as smf

# Define the regression formula
CAPM_model = smf.ols(formula='Portfolio_Excess ~ Market_Excess', data=FamaFrenchData)

# Print adjusted r-squared of the fitted regression
CAPM_fit = CAPM_model.fit()
print(CAPM_fit.rsquared_adj)

# Extract the beta
regression_beta = CAPM_fit.params['Market_Excess']
print(regression_beta)
