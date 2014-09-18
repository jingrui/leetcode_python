class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        ret = float('infinity')
        for indx, number in enumerate(num):
            left = indx + 1 
            right = len(num) -1
            while left < right:
                s = number + num[left] + num[right]
                if abs(s - target) < abs(ret - target):
                    ret = s
                if s - target > 0:
                    right -= 1
                else:
                    left += 1
        return ret

                
a = Solution()
print a.threeSumClosest([1,2,4,8,16,32,64], 82)