class Solution:
    # @return a 
    def minWindow(self, S, T):
        needtofind = dict((char,T.count(char))for char in T)
        hasfind = {}
        count = 0
        start = 0
        end = 0
        retstr = ""
        minlength = float('inf')

        while end < len(S):
            # print 'S[',start,':',(end+1),']=',S[start:end+1]

            char = S[end]
            if char in T:
                if hasfind.has_key(char):
                    hasfind[char] +=1
                else:
                    hasfind[char] = 1

                if hasfind[char] <= needtofind[char]:
                    count +=1
                # print 'hasfind[',char,']=',hasfind[char],',hasfind[char] needtofind[',char,']=',needtofind[char]
                # print 'S[',start,':',(end+1),']=',S[start:end+1],',count=',count

                if count == len(T):
                    while True:
                        key = S[start]
                        if key in T:
                            if hasfind[key] > needtofind[key]:
                                hasfind[key]-=1
                            else:
                                break
                        start +=1

                    l = end - start+1
                    if l < minlength:
                        minlength = l
                        retstr = S[start:end+1]
                    
                    hasfind[key]-=1      
                    start+=1
                    count -=1
            end+=1
        return retstr
