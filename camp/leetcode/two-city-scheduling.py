class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        diff = []
        result = 0
        for i in range(len(costs)):
            diff.append([(costs[i][0] - costs[i][1]), i])
        diff.sort()
        for i in range((len(costs))//2):
            index = diff[i][1]
            result += costs[index][0]
        for j in range((len(costs))//2,len(costs)):
            print(j)
            index = diff[j][1]
            result += costs[index][1]
        return result 