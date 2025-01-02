class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        prefix = []
        for w in words:
            if w[0] in vowels and w[-1] in vowels:
                prefix.append(1)
            else:
                prefix.append(0)
        
        for i in range(1, len(words)):
            prefix[i] = prefix[i-1] + prefix[i]
        ans = []
        for l, r in queries:
            l -= 1
            if l < 0:
                temp = prefix[r]
            else:
                temp = prefix[r] - prefix[l]
            ans.append(temp)
        return ans

         