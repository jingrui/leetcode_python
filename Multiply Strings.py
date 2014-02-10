class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        num1 = map(int,num1[::-1])
        num2 = map(int,num2[::-1])
        prod = [0 for i in range(len(num1)+len(num2))]

        for indx1,ele1 in enumerate(num1):
	        for indx2,ele2 in enumerate(num2):
	        	prod[indx1+indx2] += ele1*ele2

        carry = 0
        for indx,digit in enumerate(prod):
        	prod[indx] = (digit+carry)%10	 
        	carry = (digit+carry)/10
        prod.reverse()
        while len(prod)>0 and prod[0]==0:
            del prod[0]
        if len(prod)==0:
            return '0'
        return ''.join(map(str,prod))
