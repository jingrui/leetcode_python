class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
    	if len(s) == 0: return 0
    	n = [0 for i in range(len(s)+1)]
    	n[-1]=1
    	i = len(s)-1
    	while i >=0:
			if 1<=int(s[i])<=9:
				n[i] = n[i+1]
			if i+1 < len(s) and 10<=int(s[i])*10+int(s[i+1])<=26:
				n[i]+= n[i+2]
			i-=1
    	return n[0]
