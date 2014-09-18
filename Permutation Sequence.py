class Solution:
	# @return a string
	def getPermutation(self, n, k):
		ret = []
		base = 1
		# 0 to start index from 1
		factor = [0]
		choices = range(1, n+1)
		for i in range(1, n+1):
			base *= i
			factor.append(base)
		
		while len(choices) > 1:
			# print "n = {}, k = {}, ret = {}, choices = {}".format(n, k, ret, choices)
			indx = (k-1)/(factor[n - 1])
			ret.append(choices[indx])
			del choices[indx]
			k = (k-1) % factor[n-1] + 1
			n -= 1

		ret.append(choices[0])
		ret = map(str, ret)
		return "".join(ret)
		
			
		
a = Solution()
print a.getPermutation(4, 5)