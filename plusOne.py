class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        carry = 0
        digits = digits[::-1]
        digits[0] += 1
        for indx, digit in enumerate(digits):
            s = digit+carry
            digits[indx] = s%10
            carry = s/10
        if carry != 0:
            digits.append(carry)
        return digits[::-1]

            
        