class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        a = list(a)
        b = list(b)
        carry = 0
        ret = []
        while len(a) > 0 or len(b) > 0:
            s = carry
            if len(a) > 0:
                # print a[-1]
                s += int(a[-1])
                a.pop()
                
            if len(b) > 0:
                s += int(b[-1])
                b.pop()
            
            carry = s / 2
            ret.append(s % 2)
        if carry == 1:
            ret.append(1)
        return "".join(map(str,ret[::-1]))
            
                
            
a = Solution()
print a.addBinary("100","1")