# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root == None:
            return True

        leftq = [root.left]
        rightq = [root.right]
        leftq2 = []
        rightq2 = []
        while len(leftq)!=0 and len(rightq)!=0:
            while len(leftq)!=0 and len(rightq)!=0:
                l = leftq[0]
                del leftq[0]
                r = rightq[-1]
                del rightq[-1]
                if l == None and r == None:
                    continue
                elif l == None or r == None or l.val != r.val:
                    return False
                else:
                    leftq2.append(l.left)
                    leftq2.append(l.right)
                    rightq2.insert(0,r.right)
                    rightq2.insert(0,r.left)
            if len(leftq)!=0 or len(rightq)!=0:
                return False

            leftq,leftq2 = leftq2,[]
            rightq,rightq2 = rightq2,[]
        return True
