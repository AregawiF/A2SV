class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        mydict = {}
        left = 0
        right = 0
        ans = 0
        curr = 0
        while right < len(s):
            if s[right] not in mydict:
                mydict[s[right]] = 1
                curr += 1
                ans = max(ans, curr)
            else:
                while s[right] in mydict:
                    mydict.pop(s[left])
                    left += 1
                    curr -= 1
                mydict[s[right]] = 1
                curr += 1
            right += 1
        return ans