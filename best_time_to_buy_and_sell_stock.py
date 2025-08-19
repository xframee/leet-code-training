from typing import List

def maxProfit(prices: List[int]) -> int:
    min_price = float('inf')
    profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > profit:
            profit = price - min_price
    return profit

def maxProfit2(prices: List[int]) -> int: #sliding window apprach
    l, r = 0, 1
    max_profit = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
        else:
            l = r
        r += 1
    return max_profit

print (maxProfit2([7,1,5,3,6,4]))
print (maxProfit2([7,6,4,3,1]))
