class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        
        if len(num) ==0:
            return num
        
        # find increasing point
        indx = 0
        p = -1
        while indx+1 < len(num):
            if num[indx] < num[indx+1]:
                p = indx
            indx+=1
            
        if p == -1:
            #non increasing seq
            #reverse all
            num.sort()
        else:
            tmp = num[p+1:]
            # find the smallest that larger than point
            smallest = min([(n,i) for i,n in enumerate(tmp) if n > num[p]])
            tmp[smallest[1]],num[p] = num[p],smallest[0]
            tmp.sort()
            num[p+1:] = tmp
        return num
            
            
            
            
        
