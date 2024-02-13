# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        my_list = []
        curr = head
        while curr:
            my_list.append(curr.val)
            curr = curr.next
        left = 0
        right = 0
        for i in range(len(my_list)):
            if my_list[i] != my_list[(len(my_list)-1) -i]:
                return False
        return True
        