# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        before = dummy
        
        l = 1
        while l < left:
            before = before.next
            l += 1
        
        prev = None
        current = before.next
        rightnode = current
        
        r = left
        while r <= right:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            r += 1
        
        before.next.next = current
        before.next = prev
        
        if left == 1:
            head = prev
        return head