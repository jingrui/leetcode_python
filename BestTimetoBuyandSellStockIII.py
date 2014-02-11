# BestTimetoBuyandSellStockIII
# the idea is to find what can be earn from day 0 to day i and then from day i to day n-1
# from day i to day n-1, we need to reverse the prices so that we can know that in O(n)
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0 or len(prices) == 1:    return 0

        # from 0 to i
        low = prices[0]
        profits1 = [0]
        for price in prices[1:]:
            profits1.append(price-low)
            if price < low:
                low = price
                
        # from i to end  
        prices = prices[::-1]
        # print prices
        high = prices[0]
        profits2 = [0]
        for price in prices[1:]:
            profits2.append(high-price)
            if price > high:
                high = price

        profits2 = profits2[::-1]
        profits = []
        for ele in zip(profits1,profits2):
        	profits.append(ele[0]+ele[1])

       	return max(profits)
