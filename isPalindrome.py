class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        s = s.lower()
        start = 0
        end = len(s)-1
        while start <= end:
            if not s[start].isalpha():
                start +=1
                continue

            if not s[end].isalpha():
                end -=1
                continue

            if s[start]==s[end]:
                start +=1
                end -=1
            else:
                return False
        return True
