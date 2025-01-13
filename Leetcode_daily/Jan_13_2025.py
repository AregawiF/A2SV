class Solution:
    def minimumLength(self, s: str) -> int:
        coll = defaultdict(int)
        ans = 0
        for c in s:
            coll[c] += 1
        for key, val in coll.items():
            if val % 2 == 0:
                ans += 2
            else:
                ans += 1
        return ans