class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        ql = []
        qr = []
        count = list(s)
        for i,ele in enumerate(s):
            if ele == '(':
                ql.append(i)
            else:#')'
                if len(ql)>0:
                    top = ql[-1]
                    del ql[-1]
                    count[top]=1
                    count[i]=1
                else:
                    qr.append(i)
        # print count
        count = ''.join(map(str,count))
        # print count
        count = count.replace('(',' ')
        count = count.replace(')',' ')
        # print count
        count = count.split()
        # print count
        if len(count) == 0: return 0
        return max(map(len,count))
