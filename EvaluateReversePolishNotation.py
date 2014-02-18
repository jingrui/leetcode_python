# EvaluateReversePolishNotation
class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        tokens = map(lambda ele: int(ele)  if ele not in '+-*/' else ele,tokens)
        operators = []
        operands = []
        for token in tokens:
            if token not in list('+-*/'):
                operands.append(token)
            else:
                s = operands.pop()
                f = operands.pop()
                if token == '+':
                    r = f+s
                if token == '-':
                    r = f-s
                if token == '/':
                    sign = (f < 0 and s > 0) or (s < 0 and f >0)
                    r = abs(f)/abs(s)
                    r = -r if sign else r
                if token == '*':
                    r = f*s
                operands.append(r)
        
        return operands[0]
            
        
l = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# l = ["4", "13", "5", "/", "+"]
a = Solution()
a.evalRPN(l)
        
