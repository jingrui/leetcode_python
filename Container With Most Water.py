class Solution:
    # @return an integer
    # When we move the pointer, the width of the area decrease. If the height is smaller than the previous height, then it’s impossible that the area will increase. In other words, if left is shorter than right, no matter how you move your right pointer, you can’t find a area larger than it.
    def maxArea(self, height):
        left = 0
        right = len(height)-1
        marea = 0
        while left < right:
            marea = max(marea,(right-left)*min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return marea
            
        
        