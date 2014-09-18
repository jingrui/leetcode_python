class Solution:
	# @return a string
	def getPermutation(self, n):
		choices = range(1, n+1)
		return self.helper(n, choices)


	def helper(self, n, choices):
		if len(choices) == 1:
			return [choices]

		arr = []
		for i in choices:
			ch_cp = choices[:]
			ch_cp.remove(i)
			ret = self.helper(n, ch_cp)
			for row in ret:
				arr.append([i] + row)
		return arr

		
a = Solution()
ret = a.getPermutation(4)
for indx, row in enumerate(ret, start = 1):
	print row, indx