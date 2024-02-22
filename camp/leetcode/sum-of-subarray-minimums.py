class Solution(object):
    def sumSubarrayMins(self, arr):
        MOD = 10**9 + 7
        stack = []
        result = 0
        arr = [0] + arr + [0]  

        for i in range(len(arr)):
            while stack and arr[i] < arr[stack[-1]]:
                j = stack.pop()
                result += arr[j] * (i - j) * (j - stack[-1])
                result %= MOD
            stack.append(i)

        return result