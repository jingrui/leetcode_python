# Definition for singly-linked list.

def printList(head):
    while head!=None:
        print head.val,'->',
        head = head.next
    print

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def findMid(self,head):

        head1 = head
        slow = head
        prev = None
        fast = head
        while fast.next!=None and fast.next.next!=None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if fast.next != None:
            head2 = slow.next
            slow.next = None
        else:
            head2 = slow
            prev.next = None

        return head1, head2


    def reverseList(self,head):
        prev = None
        while head.next != None:
            next = head.next
            head.next = prev
            prev = head
            head = next

        head.next = prev
        return head


    def merge(self,l1, l2):
        # print "merge"
        # printList(l1)
        # printList(l2)
        # no need to check the l1 since it is the head of the original list
        res = l1
        cur = l1
        l1 = l1.next

        # print
        while l1!=None or l2!=None:
            # print "start"
            # printList(res)

            if l2!= None:
                cur.next = l2
                cur = cur.next
                l2 = l2.next

            if l1!=None:
                cur.next = l1
                l1 = l1.next
                cur = cur.next


            # print "end"
            # printList(res)
            # if l1 != None:
            #     print l1.val
            # else:
            #     print l1
            # if l2 != None:
            #     print l2.val
            # else:
            #     print l2

        return res



    def reorderList(self, head):
        if head == None or head.next == None or head.next.next == None:
            return head

        start1,start2 = self.findMid(head)
        # print start1.val,start2.val
        

        start2 = self.reverseList(start2)
        # print "reversed"
        # printList(start2)

        return self.merge(start1,start2)




l = ListNode(1)
head = l
for i in range(2,6):
    l.next = ListNode(i)
    l = l.next

a = Solution()
printList(head)
# printList(head)
a.reorderList(head)
printList(head)





