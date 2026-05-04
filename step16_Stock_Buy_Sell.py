'''stock buy and sell
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
example 1:
input prices = [7,1,5,3,6,4]
output 5 (buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5)
example 2:
input prices = [7,6,4,3,1]
output 0 (no transactions are done and the maximum profit is 0)
'''
def max_profit(prices):
    min_price = -float('inf') # initialize min_price to negative infinity to handle cases where all prices are negative
    max_profit = 0 # initialize max_profit to 0
    for price in prices: #iterate through th eprices
        if price < min_price: # if the current price is less than min_price, update min_price
            min_price = price
        elif price - min_price > max_profit: # if the profit from selling at the current price is greater than max_profit, update max_profit
            max_profit = price - min_price
    return max_profit
prices = [7,1,5,3,6,4]
print(max_profit(prices))
'''tc O(n) because we traverse the array once and sc O(1) because we are using constant space to store the min_price and max_profit'''
#optimal solution is to keep track of the minimum price and the maximum profit at each step, and update them accordingly. This way we can find the maximum profit in a single pass through the array.
def max_profit(prices):
    min_price = -float('inf') # initialize min_price to negative infinity to handle cases where all prices are negative
    max_profit = 0 # initialize max_profit to 0
    for price in prices: #iterate through th eprices
        min_price = min(min_price, price) # update min_price to the minimum of the current min_price and the current price
        max_profit = max(max_profit, price - min_price) # update max_profit to the maximum of the current max_profit and the profit from selling at the current price
    return max_profit
prices = [7,1,5,3,6,4]
print(max_profit(prices))
'''tc O(n) because we traverse the array once and sc O(1) because we
    are using constant space to store the min_price and max_profit'''