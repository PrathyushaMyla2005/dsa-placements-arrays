'''Stock Buy And Sell
problem Statement: You are given an array of prices where prices[i] is the price of a given stock on an ith day. 
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. 
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.'''
def stock_buy_sell(prices): # function definition
    max_profit = 0 # initialize maximum profit to 0
    for i in range(len(prices)): # iterate through the array
        for j in range(i+1, len(prices)): # iterate through the array starting from index i+1
            profit = prices[j] - prices[i] # calculate the profit for buying on day i and selling on day j
            max_profit = max(max_profit, profit) # update the maximum profit if the current profit is greater
    return max_profit # return the maximum profit
prices = [7,1,5,3,6,4] # given input array
print("Maximum profit:", stock_buy_sell(prices)) # call function and print the maximum profit
'''Time Complexity: O(n^2) where n is the number of elements in the array as we are using two nested loops to calculate the profit for all possible pairs of days.
Space Complexity: O(1) as we are using only a constant amount of extra space to store the profit and max_profit variables.'''
'''trace   the example in the code
prices = [7,1,5,3,6,4]
i = 0, j = 1, profit = 1 - 7 = -6, max_profit = max(0, -6) = 0
i = 0, j = 2, profit = 5 - 7 = -2, max_profit = max(0, -2) = 0
i = 0, j = 3, profit = 3 - 7 = -4, max_profit = max(0, -4) = 0
i = 0, j = 4, profit = 6 - 7 = -1, max_profit = max(0, -1) = 0
i = 0, j = 5, profit = 4 - 7 = -3, max_profit = max(0, -3) = 0
i = 1, j = 2, profit = 5 - 1 = 4, max_profit = max(0, 4) = 4
i = 1, j = 3, profit = 3 - 1 = 2, max_profit = max(4, 2) = 4
i = 1, j = 4, profit = 6 - 1 = 5, max_profit = max(4, 5) = 5
i = 1, j = 5, profit = 4 - 1 = 3, max_profit = max(5, 3) = 5
i = 2, j = 3, profit = 3 - 5 = -2, max_profit = max(5, -2) = 5
i = 2, j = 4, profit = 6 - 5 = 1, max_profit = max(5, 1) = 5
i = 2, j = 5, profit = 4 - 5 = -1, max_profit = max(5, -1) = 5
i = 3, j = 4, profit = 6 - 3 = 3, max_profit = max(5, 3) = 5
i = 3, j = 5, profit = 4 - 3 = 1, max_profit = max(5, 1) = 5
i = 4, j = 5, profit = 4 - 6 = -2, max_profit = max(5, -2) = 5
The maximum profit is 5, which can be achieved by buying on day 1 (price
 = 1) and selling on day 4 (price = 6).'''
def stock_buy_sell(prices): # function definition
    min_price = float('inf') # initialize minimum price to positive infinity
    max_profit = 0 # initialize maximum profit to 0
    for price in prices: # iterate through the array
        if price < min_price: # if the current price is less than the minimum price
            min_price = price # update the minimum price
        elif price - min_price > max_profit: # if the profit from selling at the current price is greater than the maximum profit
            max_profit = price - min_price # update the maximum profit
    return max_profit # return the maximum profit
prices = [7,1,5,3,6,4] # given input array
print("Maximum profit:", stock_buy_sell(prices)) # call function and print the maximum profit
'''Time Complexity: O(n) where n is the number of elements in the array as we are iterating through the array once to find the maximum profit.
Space Complexity: O(1) as we are using only a constant amount of extra space to store the min_price and max_profit variables.'''
'''trace   the example in the code
prices = [7,1,5,3,6,4]
min_price = inf, max_profit = 0
price = 7, min_price = 7, max_profit = 0
price = 1, min_price = 1, max_profit = 0
price = 5, min_price = 1, max_profit = 4
price = 3, min_price = 1, max_profit = 4
price = 6, min_price = 1, max_profit = 5
price = 4, min_price = 1, max_profit = 5
The maximum profit is 5, which can be achieved by buying on day 1 (price = 1) and selling on day 4 (price = 6).
'''