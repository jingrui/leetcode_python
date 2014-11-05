class Solution:
    def _compile(self, p):
        # Handle with a special case that the pattern string is empty
        if len(p) == 0:     return "", 0
        
        result = p[0]   # Compressed pattern
        minimal = 0     # Minimal number of chars in any matching string
        
        for i in p[1:]:
            # Count the minimal number of chars
            if i!= "*":                         minimal += 1
            
            # Compress consecutive stars into one
            if i == "*" and i == result[-1]:    continue
            else:                               result += i
        
        return result, minimal
        
    def isMatch(self, s, p):
        p, mininal = self._compile(p)
        
        # Not enough characters in s to be matched for pattern p
        if mininal > len(s):
            return False
        
        
        arr = [[False for i in range(len(p) + 1)] for j in range(len(s) + 1)]
        arr[-1][-1] = True
        for pi in range(len(arr[-1]) -2, -1 ,-1):
            if p[pi] == "*" and arr[-1][pi+1]:
                arr[-1][pi] = True
            else:
                break

        for si in range(len(arr) - 2, -1, -1):
            for pi in range(len(arr[si]) -2, -1 ,-1):
                if s[si] == p[pi] or p[pi] == "?":
                    arr[si][pi] = arr[si+1][pi+1]
                elif p[pi] == "*":
                    arr[si][pi] = arr[si+1][pi+1] or arr[si][pi+1] or arr[si+1][pi]
        return arr[0][0]
