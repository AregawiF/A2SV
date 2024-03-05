class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        right = 0
        mydict = {}
        ans = 0
        currmax = 0
        while right < len(fruits):
            if fruits[right] not in mydict:
                mydict[fruits[right]] = 1
                currmax += 1
            else:
                mydict[fruits[right]] += 1
                currmax += 1
            while len(mydict) > 2:
                if mydict[fruits[left]] > 1:
                    mydict[fruits[left]] -= 1
                else:
                    mydict.pop(fruits[left])
                currmax -= 1
                left += 1
            ans = max(ans, currmax)

            right += 1

        return ans