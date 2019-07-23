# Import the NYSE and NASDAQ listings
nyse = pd.read_excel('listings.xlsx', sheetname='nyse', na_values='n/a')
nasdaq = pd.read_excel('listings.xlsx', sheetname='nasdaq', na_values='n/a')

# Inspect nyse and nasdaq
nyse.info()
nasdaq.info()

# Add Exchange reference columns
nyse['Exchange'] = 'NYSE'
nasdaq['Exchange'] = 'NASDAQ'

# Concatenate DataFrames  
combined_listings = pd.concat([nyse, nasdaq]) 
