# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        curr1 = list1
        curr2 = list2
        dummy = ListNode()  
        list3 = dummy

        while curr1 is not None and curr2 is not None:
            if curr1.val <= curr2.val:
                list3.next = ListNode(curr1.val)
                curr1 = curr1.next
            else:
                list3.next = ListNode(curr2.val)
                curr2 = curr2.next
            list3 = list3.next

        if curr1 is not None:
            list3.next = curr1
        elif curr2 is not None:
            list3.next = curr2

        return dummy.next  
