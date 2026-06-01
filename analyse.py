import sqlite3
import matplotlib.pyplot as plt
import pandas as pd

# Connect to database
conn = sqlite3.connect('financial_data.db')

# Ask user which company to analyse
ticker = input("Enter ticker symbol to analyse: ").upper()

# Query the database
query = """
SELECT year, revenue, net_income, total_assets, total_debt, operating_cash_flow
FROM '""" + ticker + """'
ORDER BY year ASC
"""

data = pd.read_sql(query, conn)
conn.close()

# Calculate key metrics
data['profit_margin'] = (data['net_income'] / data['revenue']) * 100
data['debt_to_assets'] = (data['total_debt'] / data['total_assets']) * 100
data['revenue_growth'] = data['revenue'].pct_change() * 100

# Print summary
print(f"\n{ticker} Financial Summary:")
print(data[['year', 'profit_margin', 'debt_to_assets', 'revenue_growth']])

# Plot 1 - Revenue vs Net Income
plt.figure(figsize=(12, 5))
plt.bar(data['year'] - 0.2, data['revenue'] / 1e9, width=0.4, label='Revenue (Billions)', color='steelblue')
plt.bar(data['year'] + 0.2, data['net_income'] / 1e9, width=0.4, label='Net Income (Billions)', color='green')
plt.title(f"{ticker} — Revenue vs Net Income")
plt.xlabel("Year")
plt.ylabel("Amount (Billions)")
plt.legend()
plt.grid(True)
plt.savefig("revenue_chart.png")
print("\nRevenue chart saved!")

# Plot 2 - Profit Margin over time
plt.figure(figsize=(12, 5))
plt.plot(data['year'], data['profit_margin'], color='purple', linewidth=2, marker='o')
plt.title(f"{ticker} — Profit Margin Over Time")
plt.xlabel("Year")
plt.ylabel("Profit Margin (%)")
plt.grid(True)
plt.savefig("profit_margin_chart.png")
print("Profit margin chart saved!")

# Plot 3 - Debt to Assets ratio
plt.figure(figsize=(12, 5))
plt.bar(data['year'], data['debt_to_assets'], color='red', alpha=0.7)
plt.title(f"{ticker} — Debt to Assets Ratio Over Time")
plt.xlabel("Year")
plt.ylabel("Debt to Assets (%)")
plt.grid(True)
plt.savefig("debt_chart.png")
print("Debt chart saved!")

# Plot 4 - Operating Cash Flow
plt.figure(figsize=(12, 5))
plt.bar(data['year'], data['operating_cash_flow'] / 1e9, color='orange', alpha=0.7)
plt.title(f"{ticker} — Operating Cash Flow Over Time")
plt.xlabel("Year")
plt.ylabel("Cash Flow (Billions)")
plt.grid(True)
plt.savefig("cashflow_chart.png")
print("Cash flow chart saved!")