class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        if len(strs) == 0: return []
        if len(strs) == 1 and len(strs[0]) == 0:    return []
        
        anad = {}
        for word in strs:
            ag = ''.join(sorted(word))
            if anad.has_key(ag):
                anad[ag].append(word)
            else:
                anad[ag] = [word]
        return anad.values()
        
        
i = ['eat','tea','ate','park','ark']        
s = Solution()
print s.anagrams(i)        
