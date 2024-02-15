class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        curr = 1
        res = 0
        if target == 1:
            return 0
        else:
            if maxDoubles == 0:
                res = target - 1
            else:
                curr = target
                for _ in range(maxDoubles):
                    if curr == 1:
                        break
                    if curr % 2 == 0:
                        curr = curr // 2
                        res += 1
                    else:
                        curr = curr // 2
                        res += 2
                res += curr-1
            return res

        