class Solution:
	# @param ratings, a list of integer
	# @return an integer
	def candy(self, ratings):
		# find the botttoms
		candies = []

		for indx, rate in enumerate(ratings):
			minimum = True
			if indx != 0:
				if ratings[indx - 1] < rate:
					minimum = False
				
			if indx != len(ratings)-1:
				if ratings[indx + 1] < rate:
					minimum = False

			if minimum:
				candies.append(1)
			else:
				candies.append(None)

		# print candies
		indx = 0
		while indx < len(candies):
			candy = candies[indx]
			if candy == 1:
				previ = indx-1
				while (previ >= 0 and candies[previ] == None):
					candies[previ] = candies[previ+1] + 1
					previ -= 1

				# print previ, ratings[previ], candies[previ],candies[previ+1],candies[previ] > candies[previ+1]
				if previ >= 0 and ratings[previ] > ratings[previ+1]:
					candies[previ] = max(candies[previ], candies[previ+1] + 1)

				nexti = indx + 1
				while nexti < len(candies) and ratings[nexti] > ratings[nexti-1]:
					if ratings[nexti] == ratings[nexti-1]:
						candies[nexti] = candies[nexti-1]
					else:
						candies[nexti] = candies[nexti-1] + 1        				
					nexti += 1

				# print candies

				indx = nexti
			else:
				indx += 1

		# print candies
		# if (candies[0] == None):
		# 	return len(ratings)

		return sum(candies)




ratings = [1,3,4,3,2,1]
a = Solution()
print a.candy(ratings)





