
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                sub = False
                ind2 = 0
                ind1 = 0
                st = -1
                while ind1 < len(words[i]):
                    if words[i][ind1] == words[j][ind2]:
                        if st == -1:
                            st = ind1
                        ind2 += 1
                    else:
                        if ind2 != 0:
                            ind2 = 0
                            ind1 = st
                            st = -1
                    if ind2 == len(words[j]):
                        sub = True
                        break
                    ind1 += 1
                if sub:
                    ans.append(words[j])
        return list(set(ans))