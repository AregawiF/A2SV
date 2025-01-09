class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        preflen = len(pref)
        count = 0
        for w in words:
            if len(w) < preflen:
                continue
            ispref = True
            for i in range(preflen):
                if w[i] != pref[i]:
                    ispref = False
            if ispref:
                count += 1

        return count