class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
            
        multi = 1
        while multi < x:
            multi *= 10
        
        multi /= 10
        while x >= 10:
            # print x, multi
            left = x / multi
            right = x % 10
            if left != right:
                return False
            
            x %= multi
            x /= 10
            multi /= 100
        if x == 0: return True
        
        if multi > 100:
            return False
        else:
            return True

            
a = Solution()
print a.isPalindrome(1000000001)