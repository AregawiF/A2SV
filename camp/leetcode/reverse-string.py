class Solution:
    def reverseString(self, s: List[str], c =0, right = 0, left = 0) -> None:
        """        Do not return anything, modify s in-place instead.   """
        if len(s) == 1 or len(s) == 0:
            return
        # elif len(s) == 2:
        #     s[0], s[1] = s[1], s[0]
        if c == 0:    
            left = 0
            right = len(s)-1
        elif c == (len(s) // 2):
            return
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
        c += 1
        self.reverseString(s,c, right, left)