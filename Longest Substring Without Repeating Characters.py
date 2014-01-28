class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0: return 0
        indxdic = {}
        maxlen = 0
        starti = 0
        for indx,ele in enumerate(s):
            if indxdic.has_key(ele):
                if indx-starti > maxlen:
                    maxlen = indx-starti
                starti = max(indxdic[ele]+1,starti)
                # print 'last ',ele,' at ',indxdic[ele],',now at ',indx,',start = ',starti,',maxlen=',maxlen  

            indxdic[ele] = indx

        # print 'indx=',indx,',starti=',starti
        if indx-starti+1 > maxlen:
            maxlen = indx-starti+1
            
        return maxlen
                
        
