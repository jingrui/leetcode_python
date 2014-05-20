class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return [""]
            
        dlmap = dict()
        dlmap['2'] = "abc"
        dlmap['3'] = "def"
        dlmap['4'] = "ghi"
        dlmap['5'] = "jkl"
        dlmap['6'] = "mno"
        dlmap['7'] = "pqrs"
        dlmap['8'] = "tuv"
        dlmap['9'] = "wxyz"
        
        for key in dlmap.keys():
            dlmap[key] = list(dlmap[key])
        
        res = dlmap[digits[-1]]
        for i in range(len(digits)-2,-1,-1):
            tmp = []
            for letter in dlmap[digits[i]]:
                for cur in res:
                    tmp.append(letter+cur)
            res = tmp
        return res
            
            
        
        
