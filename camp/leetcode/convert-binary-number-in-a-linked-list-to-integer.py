# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        length = 0
        curr = head
        result = 0
        while curr:
            length += 1
            curr = curr.next
        current = head
        for i in range(length-1, -1,-1):
            # if not current:
            #     break
            result += (2 ** i) * current.val
            current = current.next
        return result

