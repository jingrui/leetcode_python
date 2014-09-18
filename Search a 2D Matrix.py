class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        for row in range(len(matrix)):
            if target > matrix[row][-1]:
                continue
            else:
                break
            
        return self.binarySearch(matrix[row], 0 ,len(matrix[row])-1, target)
    
    def binarySearch(self, l, start, end, target):
        if start == end:
            if l[start] != target:
                return False
            else:
                return True
        
        mid = (start+end)/2
        if l[mid] == target:
            return True
        elif l[mid] < target:
            return self.binarySearch(l, mid+1, end, target)
        else:
            return self.binarySearch(l, start, mid, target)
        