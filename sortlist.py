# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
    	length = 0
    	cur = head
    	while cur!= None:
    		cur = cur.next
    		length+=1
    	# print length

    	def merge(h1,h2):
    		# print  'merge'
    		# print h1.val
    		# print h2.val
    		if h1 == None:
    			return h2
    		if h2 == None:
    			return h1

    		if h1.val < h2.val:
    			ret = h1
    			h1 = h1.next
    		else:
    			ret = h2
    			h2 = h2.next

    		h = ret

    		while h1!= None or h2!=None:

    			if h1 == None:
    				ret.next = h2
    				h2 = h2.next
    			elif h2 == None:
    				ret.next = h1
    				h1 = h1.next
    			elif h1.val < h2.val:
    				ret.next = h1
    				h1 = h1.next
    			else:
    				ret.next = h2
    				h2 = h2.next
    			ret = ret.next

    		# printlist(h)
    		return h



    	def helper(h,l):
    		if l <= 1:
    			return h

    		mid = l/2
    		indx = 0
    		h2 = h
    		while indx < mid-1:
    			h2 = h2.next
    			indx+=1
    		next = h2.next
    		h2.next = None
    		h2 = next

    		t1 = h
    		t2 = h2
    		# print
    		# printlist(t1)
    		# print mid
    		# printlist(t2)
    		# print l-mid
    		left = helper(h,mid)
    		right = helper(h2,l-mid)

    		return merge(left,right)

    	return helper(head,length)

        

def printlist(node):
	while node!= None:
		print node.val,'->',
		node = node.next
	print 

head = ListNode(5)
cur = head
for i in range(4,-1,-1):
	cur.next = ListNode(i)
	cur = cur.next

cur = head
# printlist(cur)

a = Solution()
head = a. sortList(cur)
printlist(head)



