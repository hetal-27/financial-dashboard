import yfinance as yf
import sqlite3
import pandas as pd

# Company to analyse
ticker = input("Enter ticker symbol (e.g. RELIANCE.NS, TCS.NS, AAPL): ").upper()

# Download financial data
company = yf.Ticker(ticker)

# Get financial statements
income_statement = company.financials
balance_sheet = company.balance_sheet
cash_flow = company.cashflow

# Extract income statement data
revenue = income_statement.loc['Total Revenue']
net_income = income_statement.loc['Net Income']

# Extract balance sheet data
total_assets = balance_sheet.loc['Total Assets']
total_debt = balance_sheet.loc['Total Debt']

# Extract cash flow data
operating_cash_flow = cash_flow.loc['Operating Cash Flow']

# Create clean dataframe
data = pd.DataFrame({
    'year': revenue.index.year,
    'revenue': revenue.values,
    'net_income': net_income.values,
    'total_assets': total_assets.values,
    'total_debt': total_debt.values,
    'operating_cash_flow': operating_cash_flow.values
})

print("\nClean Data:")
print(data)

# Store in SQL database
conn = sqlite3.connect('financial_data.db')
data.to_sql(ticker, conn, if_exists='replace', index=False)
conn.close()

print(f"\nData saved to financial_data.db!")

