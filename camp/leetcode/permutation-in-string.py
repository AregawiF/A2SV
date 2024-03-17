class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1dict = {}
        s2dict = {}
        for c in s1:
            if c in s1dict:
                s1dict[c] += 1
            else:
                s1dict[c] = 1
        left = 0
        right = 0
        while right < len(s2):
            if s2[right] not in s1dict:
                s2dict.clear()
                left = right + 1
            else:
                if s2[right] in s2dict:
                    if s2dict[s2[right]] < s1dict[s2[right]]:
                        s2dict[s2[right]] += 1
                    else:
                        while s2dict[s2[right]] >= s1dict[s2[right]]:
                            if s2[left] == s2[right]:
                                s2dict[s2[right]] -= 1
                            else:
                                s2dict[s2[left]] -= 1
                            left += 1
                        s2dict[s2[right]] += 1
                else:
                    s2dict[s2[right]] = 1
            if s2dict == s1dict:
                return True 
            right += 1

        return False



