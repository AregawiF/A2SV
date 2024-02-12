class Solution(object):
    def shiftingLetters(self, s, shifts):
        range_sum = [0] * (len(s)+1)
        for shift in shifts:
            if shift[2] == 0:
                range_sum[shift[0]] -= 1
                range_sum[shift[1]+1] += 1
            else:
                range_sum[shift[0]] += 1
                range_sum[shift[1]+1] -= 1

        for i in range(1,len(range_sum)):
            range_sum[i] = range_sum[i] + range_sum[i-1] 
        result = ""
        print(range_sum)
        for i in range(len(s)):
            current = ord(s[i]) - ord('a')
            current=(current+range_sum[i])%26
            result += chr(97+ current)
        return result
