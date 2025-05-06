def max_profit(prices):
    min_price = float('inf')  # Start with a very high min
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price  # Found a new lower buying price
        profit = price - min_price  # If sold today
        if profit > max_profit:
            max_profit = profit  # Update max profit

    return max_profit

# Example
prices = [7, 1, 5, 3, 6, 4]
print("Max Profit:", max_profit(prices))  # Output: 5
