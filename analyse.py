import sqlite3
import matplotlib.pyplot as plt
import pandas as pd

# Connect to database
conn = sqlite3.connect('financial_data.db')

# Ask user which company to analyse
ticker = input("Enter ticker symbol to analyse: ").upper()

# Query the database using SQL
query = """
SELECT year, revenue, net_income
FROM '""" + ticker + """'
ORDER BY year ASC
"""

data = pd.read_sql(query, conn)
conn.close()

print("\nData from database:")
print(data)

# Calculate profit margin
data['profit_margin'] = (data['net_income'] / data['revenue']) * 100

print("\nProfit Margins:")
print(data[['year', 'profit_margin']])

# Plot Revenue vs Net Income
plt.figure(figsize=(12, 5))
plt.bar(data['year'] - 0.2, data['revenue'] / 1e9, width=0.4, label='Revenue (Billions)', color='steelblue')
plt.bar(data['year'] + 0.2, data['net_income'] / 1e9, width=0.4, label='Net Income (Billions)', color='green')
plt.title(f"{ticker} — Revenue vs Net Income")
plt.xlabel("Year")
plt.ylabel("Amount (Billions)")
plt.legend()
plt.grid(True)
plt.savefig("revenue_chart.png")
print("\nChart saved!")
