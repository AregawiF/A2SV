class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        block_arr = []
        res = [len(blocks)] * len(blocks)
        colors = []
        for string in blocks:
            block_arr.append(string)
        for i in range(len(block_arr)):
            if k+i > len(blocks):
                break
            colors.append(block_arr[i:k+i])
        for i in range(len(colors)):
            res[i] = 0
            for color in colors[i]:
                if color == "W":
                    res[i] += 1
        result = min(res)
        return result
