class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """
        prefix_sum = [0] * (len(customers)+1)
        suffix_sum = [0] * (len(customers)+1)
        for i in range(1, len(customers)+1):
            if customers[i-1] == "N":
                suffix_sum[i] = suffix_sum[i-1] + 1
            elif customers[i-1] == "Y":
                suffix_sum[i] = suffix_sum[i-1] + 0
        for i in range(len(prefix_sum)-2, -1, -1):
            if customers[i] == "Y":
                prefix_sum[i] = prefix_sum[i+1] + 1
            elif customers[i] == "N":
                prefix_sum[i] = prefix_sum[i+1] + 0    
        result = float('inf')
        index = -1
        for i in range(len(customers)+1):
            current = prefix_sum[i] + suffix_sum[i]
            
            if current < result:
                result = current
                index = i
        return index



        