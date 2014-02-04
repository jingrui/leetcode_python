'''
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return True.
When s3 = "aadbbbaccc", return False.
'''

'''
idea:
def is(p1,p2,p3):
	ret1 = is(p1+1,p2,p3+1) if s1[p1] == s3[p3] else false
	ret2 = is(p1,p2+1,p3+1) if s2[p2] == s3[p3] else false
	return ret1 or ret2

optimal:
def is(p1,p2,p3):
	ret1 = is(p1+1,p2) if s1[p1] == s3[p1+p2] else false
	ret2 = is(p1,p2+1) if s2[p2] == s3[p1+p2] else false
	return ret1 or ret2
'''


class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
    	#==========================best solution================
    	# O(n^2)
		def isdp2d():
			array = [[False for p2 in range(len(s2)+1)]for p1 in range(len(s1)+1)]
			for p1 in range(len(s1),-1,-1):
				for p2 in range(len(s2),-1,-1):
					if p1 == len(s1) and p2 == len(s2) and (p1+p2) == len(s3):
						array[p1][p2]=True
					else:
						ret1 = array[p1+1][p2] if p1+1<= len(s1) and p1+p2+1<= len(s3) and s1[p1] == s3[p1+p2] else False
						ret2 = array[p1][p2+1] if p2+1<= len(s2) and p1+p2+1<= len(s3) and s2[p2] == s3[p1+p2] else False
						array[p1][p2] = ret1 or ret2
			# for ele in array:
			# 	print ele
			return array[0][0]
		return isdp2d()



		#O(3^n)
        def interstr(p1,p2,p3):
        	if p1 == len(s1) and p2 == len(s2) and p3 == len(s3):	return True
        	ret1 = interstr(p1+1,p2,p3+1) if p1 < len(s1) and p3 < len(s3) and s1[p1] == s3[p3] else False
        	ret2 = interstr(p1,p2+1,p3+1) if p2 < len(s2) and p3 < len(s3) and s2[p2] == s3[p3] else False
        	return ret1 or ret2
        # return interstr(0,0,0)

        # O(n^3)
        def isdp3d():
        	cube = {}
        	for p3 in range(len(s3)+1):
        		for p1 in range(len(s1)+1):
        			for p2 in range(len(s2)+1):
        				cube[(p1,p2,p3)]=False
        	# cube[(p1,p2,p3)] = True

        	# print sorted(cube.items())
        	for p3 in range(len(s3),-1,-1):
        		for p1 in range(len(s1),-1,-1):
        			for p2 in range(len(s2),-1,-1):
        				if p1 == len(s1) and p2 == len(s2) and p3 == len(s3):
        					cube[(p1,p2,p3)]=True
        				else:
        					ret1 = cube[(p1+1,p2,p3+1)] if p1+1<= len(s1) and p3+1<= len(s3) and s1[p1] == s3[p3] else False
        					ret2 = cube[(p1,p2+1,p3+1)] if p2+1<= len(s2) and p3+1<= len(s3) and s2[p2] == s3[p3] else False
        					cube[(p1,p2,p3)]=ret1 or ret2
        	return cube[(0,0,0)]
        # return isdp()

s = Solution()
s1 = 'aabcc'
s2 = 'dbbca'
s3 = 'aadbbcbcac'
s4 = 'aadbbbaccc'
print s.isInterleave(s1,s2,s4)





        
