class Solution:
	# @param words, a list of strings
	# @param L, an integer
	# @return a list of strings
	def fullJustify(self, words, L):
		
		ret = []

		line = [words[0]]
		del words[0]
		length = len(line[0])
		while (len(words) > 0):
			
			if length + 1 + len(words[0]) <= L:
				line.append(" ")
				line.append(words[0])
				length += 1 + len(words[0])
				del words[0]
			else:
				extra = L - length
				if len(line) == 1:
					line = line[0] + " " * extra
				else:
					indx = -1
					while extra > 0:
						indx = (indx + 2) % (len(line)-1)
						line[indx] += " "
						extra -= 1
				ret.append("".join(line))

				line = [words[0]]
				del words[0]
				length = len(line[0])
			
		extra = L - length
		line.append(" " * extra)
		ret.append("".join(line))
		return ret



words = ["What","must","be","shall","be."]
L = 12
a = Solution()
print a.fullJustify(words, L)


		
			
