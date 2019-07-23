# Import the data
nyse = pd.read_excel('listings.xlsx', sheetname = 'nyse', na_values= 'n/a')

# Display the head of the data
print(nyse.head(10))

# Inspect the data
nyse.info()
