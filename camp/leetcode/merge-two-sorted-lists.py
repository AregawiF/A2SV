# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def merge(curr1, curr2):
            if curr1 is None:
                return curr2
            elif curr2 is None:
                return curr1
            
            if curr1.val <= curr2.val:
                curr1.next = merge(curr1.next, curr2)
                return curr1
            else:
                curr2.next = merge(curr1, curr2.next)
                return curr2
        
        return merge(list1, list2)