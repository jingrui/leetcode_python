class Solution:
	# @param S, a string
	# @param L, a list of string
	# @return a list of integer
	def findSubstring(self, S, L):
		ret = []
		length = len(L[0])
		wordSet = set(L)
		indx = 0
		left = indx
		found = {}
		needFound = {}
		for word in L:
		    needFound[word] = L.count(word)
		    
		
		while indx+length <= len(S):
			word = S[indx: indx+length]
			if word in wordSet:
				if not found.has_key(word):
					found[word] = []
				elif len(found[word]) >= needFound[word]:
					left = max(left, found[word][0] + length)
					del found[word][0]

				found[word].append(indx)
				indx += length

				print "indx = {}, word = {}, found = {}, needFound = {},left = {}, len(L)*length = {}".format(indx, word, found[word], needFound[word], left, len(L)*length)
				if indx - left == len(L)*length:
					ret.append(left)
					left += length
					indx = left
					found = {}
			else:
				print  "indx = {}, word = {}, left = {} not found".format(indx, word,left)
				indx += 1
				left = indx
		return ret


a = Solution()
print a.findSubstring("abaababbaba",\
	["ab","ba","ab","ba"])


class SolutionSlow:
	# running time O(S*L*lengthofEachWordInL)))
	# @param S, a string
	# @param L, a list of string
	# @return a list of integer
	def findSubstring(self, S, L):
		length = len(L[0])
		ret = []
		wordSet = set(L)
		for i, word in enumerate(S):
			indx = i
			wordSet = set(L)
			while len(wordSet) != 0:

				word = S[indx: indx + length]
				if word in wordSet:
					wordSet.remove(word)
					indx += length
				else:
					break
			if len(wordSet) == 0:
				ret.append(i)
		return ret
