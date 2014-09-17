class Solution:
    # @return an integer
    def romanToInt(self, s):
        unit = dict()
        unit["I"] = 1
        unit["V"] = 5
        unit["X"] = 10
        unit["L"] = 50
        unit["C"] = 100
        unit["D"] = 500
        unit["M"] = 1000

        ret = 0
        for indx, u in enumerate(s):
            if indx +1 < len(s):
                if unit[s[indx +1]] > unit[u]:
                    ret -= unit[u]
                else:
                    ret += unit[u]
            else:
                ret += unit[u]
        return ret
            
a = Solution()
print a.romanToInt("MCMXCVI")