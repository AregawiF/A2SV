class Solution: 
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        sh = [0] * (n + 1)  
        end = []  
        for start, end, direction in shifts:
            if direction == 1: 
                sh[start] += 1
                if end + 1 < n:
                    sh[end + 1] -= 1
            else: 
                sh[start] -= 1
                if end + 1 < n:
                    sh[end + 1] += 1

        cumulative = 0
        for i in range(n):
            cumulative += sh[i]
            sh[i] = cumulative

        result = []
        for i in range(n):
            val = (ord(s[i]) - 97 + sh[i]) % 26
            result.append(chr(97 + val))
        return "".join(result)
