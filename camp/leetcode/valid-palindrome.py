class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        vals = list([val for val in s if val.isalpha() or val.isnumeric()])
        new_str = "".join(vals)
        print(new_str)
        left = 0
        right = len(new_str)-1
        print(left,right)
        while left<= right:
            if new_str[left] != new_str[right]:
                return False
            left +=1
            right -= 1
        return True
        