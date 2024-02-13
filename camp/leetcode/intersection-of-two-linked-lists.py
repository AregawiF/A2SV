# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        my_dict = {}
        dummyA = ListNode(0)
        dummyA.next = headA
        dummyB = ListNode(0)
        dummyB.next = headB
        curr = dummyA
        while curr:
            my_dict[curr.next] = 0
            curr = curr.next
        current = dummyB
        while current:
            if current.next in my_dict:
                return current.next
            current = current.next
        
        