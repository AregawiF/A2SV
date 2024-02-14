class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """

        prefix = [0] * (len(s) + 1) 
        suffix = [0] * (len(s) + 1) 
        s_list = [int(char) for char in s]
        for i in range(len(s)):
            if s_list[i] == 0:
                prefix[i+1] = prefix[i] + 1
            else:
                prefix[i+1] = prefix[i]
            
        for i in range(len(s)-1, -1, -1):
            if s_list[i] == 1:
                suffix[i] = suffix[i+1] + 1
            else:
                suffix[i] = suffix[i+1]
        result = 0
        for i in range(1,len(prefix)-1):
            result = max(result, (prefix[i] + suffix[i]))
        return result