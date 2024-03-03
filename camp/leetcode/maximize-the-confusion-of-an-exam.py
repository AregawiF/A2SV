class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = 0
        right = 0
        ans = 0
        countF = 0
        countT = 0
        while right < len(answerKey):
            if answerKey[right] == "F":
                countF += 1
            while countF > k:
                if answerKey[left] == "F":
                    countF -= 1
                left += 1
            ans = max(ans, (right - left)+1)
            right += 1
        left = 0
        right = 0
        while right < len(answerKey):
            if answerKey[right] == "T":
                countT += 1
            while countT > k:
                if answerKey[left] == "T":
                    countT -= 1
                left += 1
            ans = max(ans, (right - left)+1)
            right += 1
        return ans