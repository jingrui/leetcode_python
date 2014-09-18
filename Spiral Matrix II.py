class Solution:
	# @return a list of lists of integer
	def generateMatrix(self, n):
		number = 1
		ret = [[0 for i in range(n)] for j in range(n)]
		loop = 0
		while number <= n * n:

			row = loop
			for col, num in enumerate(ret[row]):
				if ret[row][col] == 0:
		   			ret[row][col] = number
					number += 1
			
			col = n - loop - 1
			for row, num in enumerate(ret[col]):
				if ret[row][col] == 0:
		   			ret[row][col] = number
					number += 1
				
			row = n - loop - 1
			for col in range(len(ret[row])-1, -1, -1):
				if ret[row][col] == 0:
		   			ret[row][col] = number
					number += 1
				
			col = loop
			for row in range(len(ret[col])-1, -1, -1):
				if ret[row][col] == 0:
		   			ret[row][col] = number
					number += 1
				
			loop += 1
			
		return ret
		
			
a = Solution()
ret = a.generateMatrix(4)
for row in ret:
	print row