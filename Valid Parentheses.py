class Solution:
    # @return a boolean
    def isValid(self, s):
        q = []
        left = '({['
        for ele in s:
            if ele in left:
                q.append(ele)
            else:
                if len(q) == 0: return False
                top = q[-1]
                del q[-1]
                if  not ((ele == ')' and top == '(') or
                    (ele == ']' and top == '[') or
                    (ele == '}' and top == '{')):
                    return False
            
        return True if len(q)==0 else False
