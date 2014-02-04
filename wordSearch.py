class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        wordloc = {}
        for indxr,row in enumerate(board):
            for indxc,ele in enumerate(row):
                if wordloc.has_key(ele):
                    wordloc[ele].append((indxr,indxc))
                else:
                    wordloc[ele]=[(indxr,indxc)]
                    
        # check if has corresponding number of character            
        def checkfreq():
            freq = {}
            for char in word:
                if freq.has_key(char):
                    freq[char]+=1
                else:
                    freq[char] = 1

            for key in freq.keys():
                if not wordloc.has_key(key) or freq[key]!= len(wordloc[key]):
                    return False
            return True
            
        def checknei(loc1,loc2):
            if loc2 != None:
                return abs(loc1[0]-loc2[0])+abs(loc1[1]-loc2[1]) == 1
            else:
                return True
        
        # check if word char is close to each other
        def checkloc(indx,used,prev):
            if indx == len(word):   return True
            if wordloc.has_key(word[indx]):
                ret = []
                for loc in wordloc[word[indx]]:
                    if loc not in used and checknei(loc,prev):
                        uc = used[:]+[loc]
                        ret.append(checkloc(indx+1,uc,loc))
                return any(ret)
            else:
                return False
        
        return checkfreq() and checkloc(0,[],None)
                        
# b = ['aaaa','aaaa','aaaa','aaaa','aaab']
b = ['a']
# w = 'aaaaaaaaaaaaaaaaaaaa'
w = 'a'
s = Solution()
print s.exist(b,w)
        
        
            
        
