class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left = 0
        answer = 0
        for string in s:
            if string == ")" and left == 0:
                answer += 1
            elif string == "(":
                left += 1
                answer += 1
            else:
                left -= 1
                answer -= 1     
        return answer