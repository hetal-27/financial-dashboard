import yfinance as yf
import sqlite3
import pandas as pd

# Company to analyse
ticker = input("Enter ticker symbol (e.g. RELIANCE.NS, TCS.NS, AAPL): ").upper()

# Download financial data
company = yf.Ticker(ticker)

# Get income statement
income_statement = company.financials

# Extract the rows we care about
revenue = income_statement.loc['Total Revenue']
net_income = income_statement.loc['Net Income']

# Create a clean dataframe
data = pd.DataFrame({
    'year': revenue.index.year,
    'revenue': revenue.values,
    'net_income': net_income.values
})

print("\nClean Data:")
print(data)

# Store in SQL database
conn = sqlite3.connect('financial_data.db')
data.to_sql(ticker, conn, if_exists='replace', index=False)
conn.close()

print(f"\nData saved to financial_data.db!")

