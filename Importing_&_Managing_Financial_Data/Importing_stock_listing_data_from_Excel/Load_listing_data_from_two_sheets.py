# Create pd.ExcelFile() object
xls = pd.ExcelFile('listings.xlsx')

# Extract sheet names and store in exchanges
exchanges = xls.sheet_names

# Create listings dictionary with all sheet data
listings = pd.read_excel(xls, sheetname=['amex', 'nasdaq', 'nyse'], na_values='n/a')

# Inspect NASDAQ listings
listings['nasdaq'].info()
