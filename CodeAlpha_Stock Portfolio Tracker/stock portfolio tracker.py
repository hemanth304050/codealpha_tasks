# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 135,
    "MSFT": 400
}

print("Stock Portfolio Tracker")
print("Available stocks:", list(stock_prices.keys()))
print("Enter 'done' to stop adding stocks.\n")

portfolio = []
total_value = 0

while True:
    stock = input("Enter stock symbol: ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not found. Try again.\n")
        continue

    qty = input("Enter quantity: ")

    if not qty.isdigit():
        print("Invalid quantity.\n")
        continue

    qty = int(qty)
    price = stock_prices[stock]
    value = price * qty
    total_value += value

    portfolio.append((stock, qty, price, value))
    print(f"{stock} added. Value = {value}\n")

print("Total Investment Value:", total_value)

# Save to text file
with open("portfolio.txt", "w") as f:
    f.write("Stock\tQty\tPrice\tValue\n")
    for s, q, p, v in portfolio:
        f.write(f"{s}\t{q}\t{p}\t{v}\n")
    f.write(f"\nTotal Investment: {total_value}")

# Save to CSV file
with open("portfolio.csv", "w") as f:
    f.write("Stock,Quantity,Price,Value\n")
    for s, q, p, v in portfolio:
        f.write(f"{s},{q},{p},{v}\n")
    f.write(f"\nTotal,{total_value}")
