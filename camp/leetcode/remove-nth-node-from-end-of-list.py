# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode()
        dummy.next = head
        if head.next == None:
            return
        prev = dummy
        left,right = head, head
        for _ in range(1,n):
            right = right.next
        while right.next:
            prev = left
            left = left.next
            right = right.next
        prev.next = left.next
        left.next = None
        head = dummy.next
        return head
        

        
