class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s = s.split(" ")
        i = 0
        # print s
        while i < len(s):
        	if s[i]=="":
        		del s[i]
        	else:
	            i+=1

        # print s
        s = s[::-1]
        return " ".join(s)
    
a = Solution()
s =  "the sky is blue"
print a.reverseWords(s)
