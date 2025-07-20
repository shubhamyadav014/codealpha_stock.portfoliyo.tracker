import csv

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "AMZN": 140,
    "GOOGL": 130
}

portfolio = {}

# Taking user input for stock quantities
print("Enter your stock quantities (type 'done' to finish):")
while True:
    stock = input("Stock symbol (e.g., AAPL, TSLA): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not found in our price list! Available:", ", ".join(stock_prices.keys()))
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Please enter a valid number!")

# Calculate total investment
total_investment = 0
print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    value = qty * stock_prices[stock]
    total_investment += value
    print(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${value}")

print(f"\nTotal Investment Value = ${total_investment}")

# Optional: Save to file
save = input("Do you want to save this portfolio? (yes/no): ").lower()
if save == "yes":
    with open("portfolio.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price", "Total Value"])
        for stock, qty in portfolio.items():
            writer.writerow([stock, qty, stock_prices[stock], qty * stock_prices[stock]])
        writer.writerow(["Total", "", "", total_investment])
    print("Portfolio saved as portfolio.csv")
