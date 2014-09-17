# Definition for a point
class Point:
	def __init__(self, a=0, b=0):
		self.x = a
		self.y = b

class Solution:
	# @param points, a list of Points
	# @return an integer
	def maxPoints(self, points):
		if len(points) < 2:
			return len(points)
			
		maxNum = 0
		for indx, origin in enumerate(points, start = 1):

			slopes = {}
			dup = 0
			for indx2, point in enumerate(points, start = 1):
				if indx == indx2:
					continue

				if origin.x == point.x and origin.y == point.y:
					dup += 1
					continue
					
				print "{} {}, {} {}".format(origin.x, origin.y, point.x, point.y)
				deltay = point.y - origin.y
				deltax = point.x - origin.x
				if deltay == 0:
					slope = 0
				elif deltax == 0:
					slope = float("infinity")
				else:
					slope = deltay / float(deltax)

				if slopes.has_key(slope):
					slopes[slope] = slopes[slope] + 1
				else:
					slopes[slope] = 1

				print slopes

			if len(slopes) != 0:
				maxNum = max(maxNum, max(slopes.values()) + dup + 1)
			else:
				maxNum = max(maxNum, dup + 1)

		return maxNum

def pointList(l):
	ret = []
	for t in l:
		ret.append(Point(t[0], t[1]))
	return ret


a = Solution()
points = pointList([(84,250),(0,0),(1,0),(0,-70),(0,-70),(1,-1),(21,10),(42,90),(-42,-230)])
print a.maxPoints(points)

