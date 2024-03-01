class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pdict = {}
        sdict = {}
        ans = []
        if len(s) < len(p):
            return ans
        for c in p:
            if c not in pdict:
                pdict[c] = 1
            else:
                pdict[c] += 1
        left = 0
        right = 0
        while right < len(s):
            while right < len(p):
                if s[right] not in sdict:
                    sdict[s[right]] = 1
                else:
                    sdict[s[right]] += 1
                if right == len(p)-1:
                    break
                right += 1
            
            if sdict == pdict:
                ans.append(left)
            if right == len(s)-1:
                return ans
            sdict[s[left]] -= 1
            if sdict[s[left]] == 0:
                sdict.pop(s[left])
            right += 1
            left += 1
            if s[right] not in sdict:
                sdict[s[right]] = 1
            else:
                sdict[s[right]] += 1

        return ans