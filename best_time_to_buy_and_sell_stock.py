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

print (maxProfit([7,1,5,3,6,4]))
print (maxProfit([7,6,4,3,1]))
