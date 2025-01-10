class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        ans = []
        pat = [0] * 26
        for w in words2:
            temp = [0] * 26
            for c in w:
                val = ord(c) - 97
                temp[val] += 1
        
            for i in range(26):
                pat[i] = max(pat[i], temp[i])

        for w in words1:
            uni = True
            curr = [0] * 26
            for c in w:
                ind = ord(c) - 97
                curr[ind] += 1

            for i in range(26):
                if pat[i] > curr[i]:
                    uni = False
                    break

            if uni:
                ans.append(w)

        return ans