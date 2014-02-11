# BestTimetoBuyandSellStockIII
# the idea is to find what can be earn from day 0 to day i and then from day i to day n-1
# from day i to day n-1, we need to reverse the prices so that we can know that in O(n)
# BestTimetoBuyandSellStockIII
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0 or len(prices) == 1:    return 0

        # from 0 to i
        low = prices[0]
        maxp = 0
        profits1 = [0]
        for price in prices[1:]:
        	p = price-low
        	if p > maxp:
        		maxp = p

        	profits1.append(maxp)
        	if price < low:
        		low = price        
        # print prices
        # print profits1,'\n'


        # from i to end  
        prices = prices[::-1]
        high = prices[0]
        profits2 = [0]
        maxp = 0
        for price in prices[1:]:
        	p = high-price
        	if p > maxp:
        		maxp = p
        	profits2.append(maxp)
        	if price > high:
        		high = price
        # print profits2
        prices = prices[::-1]
        profits2 = profits2[::-1]
        # print profits2
        profits = []
        for ele in zip(profits1,profits2):
        	profits.append(ele[0]+ele[1])
        # print profits
        return max(profits) if max(profits)>0 else 0
