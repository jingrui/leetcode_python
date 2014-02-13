# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head == None or head.next == None:
            return head
        
        next = head.next
        ret = self.swapPairs(next.next)
        head.next = ret
        next.next = head
        return next
        
