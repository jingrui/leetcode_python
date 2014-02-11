class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices)==0: return 0
        
        # buy at each low point and sell at each high point
        low = prices[0]
        profit = 0
        for indx,price in enumerate(prices[:]):
            if indx==0:continue
            # decreasing
            if price < prices[indx-1]:
                profit+=prices[indx-1]-low
                low = price
                
        profit+= prices[-1]-low
        return profit
                
