class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
    	ret = []
        s = set(num)
        # print s
        for ele in num:
        	if ele in s:
        		l = [ele]
        		
        		s.discard(ele)
        		# smaller
        		sele = ele
        		sele -=1
        		while sele in s:
        			s.discard(sele)
        			l.insert(0,sele)
        			sele-=1
        		# larger
        		lele = ele
        		lele +=1
        		while lele in s:
        			s.discard(lele)
        			l.append(lele)
        			lele +=1
        		ret.append((len(l),l))
        return max(ret)[0]
        


l = [100, 4, 200, 1, 3, 2]
a = Solution()
print a.longestConsecutive(l)        
