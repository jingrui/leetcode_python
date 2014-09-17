class Solution:
	# @param s, a string
	# @return a boolean
	def isNumber(self, s):
		s = s.lower()
		s = s.strip().split("e")
		if len(s) > 2:
			return False
		elif len(s) == 1:
		    s[0] = self.removeSign(s[0])
		    return len(s[0]) > 0 and self.checkDouble(s[0])
		else:
			s[0] = self.removeSign(s[0])
			s[1] = self.removeSign(s[1])
			return len(s[0]) > 0 and self.checkDouble(s[0]) and \
				len(s[1]) > 0 and self.checkInt(s[1])


	def removeSign(self, s):
		indx = 0
		for indx in range(len(s)):
			if s[indx] not in "+-":
				break
		return s[indx:]

	def checkDouble(self, s):

		if s.count(".") > 1:
			return False

		ret = True
		NonEmpty = 0
		for indx, ss in enumerate(s.split("."), start=1):
			ret &= self.checkInt(ss)
			if len(ss) != 0:
				NonEmpty += 1
		return ret and NonEmpty > 0

		

	def checkInt(self, s):
		for letter in s:
			if letter not in "0123456789":
				return False
		return True




numbers = [" 005047e+6", "-1.", ". 1", "..2","3.", "1","22","3.3", " 1e 2", "1.2 E3", "5a6","e" , "." , ".1", "0e"]
a = Solution()
for number in numbers:
	print number,
	print a.isNumber(number)