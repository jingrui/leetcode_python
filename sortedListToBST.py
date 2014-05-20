# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        if head == None:
            return None
        
        if head.next == None:
            return TreeNode(head.val)
            
        if head.next.next == None:
            root = TreeNode(head.val)
            root.right = TreeNode(head.next.val)
            return root
        
        # find the middle one
        first = head
        second = head
        
        while second.next != None and second.next.next != None:
            first = first.next
            second = second.next.next
        
        # left
        tailleft = head
        while tailleft.next != first:
            tailleft = tailleft.next
        
        tailleft.next = None
        
        # right
        headright = first.next
        first.next = None
        root = TreeNode(first.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(headright)
        return root
            
        
    
        
