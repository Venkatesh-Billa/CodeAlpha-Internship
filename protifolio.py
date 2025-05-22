# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 300
}

portfolio = {}

# Input number of different stocks
n = int(input("Enter number of different stocks: "))

# Take user input for stock name and quantity
for _ in range(n):
    stock = input("Enter stock name (e.g., AAPL): ").upper()
    qty = int(input(f"Enter quantity of {stock}: "))
    if stock in stock_prices:
        portfolio[stock] = qty
    else:
        print(f"Stock {stock} not found in prices list.")

# Calculate and display total investment
total_investment = 0
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = qty * price
    total_investment += value
    print(f"{stock}: {qty} shares × ${price} = ${value}")

print("\nTotal Investment Value: $", total_investment)

# Save to .txt file
with open("portfolio.txt", "w") as f:
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = qty * price
        f.write(f"{stock}: {qty} shares × ${price} = ${value}\n")
    f.write(f"\nTotal Investment Value: ${total_investment}")
