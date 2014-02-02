class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if (x == 0):	return 0
        last = 0.0
        res = 1.0
        while (res != last):
            last = res
            res = (res + x / res) / 2
    
        return int(res)
        
