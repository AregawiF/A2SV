class Solution:
    def longestPalindrome(self, s: str) -> int:
        strdict = {}
        ones = 0
        res = 0
        for letter in s:
            if letter in strdict:
                strdict[letter] += 1
            else: strdict[letter] = 1
        for key, val in strdict.items():
            if val % 2 == 0:
                res += val
            else:
                if ((val-1) % 2 == 0) and ((val-1) != 0):
                    res += val-1
                    ones += 1
                ones += 1
        if ones != 0:
            res += 1
        return res
