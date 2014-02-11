class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0 or len(prices) == 1:    return 0
        low = prices[0]
        profits = []
        for price in prices[1:]:
            profits.append(price-low)
            if price < low:
                low = price
        return max(profits) if max(profits)>0 else 0
                
        
