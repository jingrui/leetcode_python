class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        q= []
        longest = 0
        count = 0
        for ele in s:
            if ele == '(':
                q.append('(')
            else:
                if len(q)>0:
                    top = q[-1]
                    if top == '(':
                        count +=1
                        del q[-1]
                    else:
                        count = 0
            longest = count if count > longest else longest
        return longest*2
            
