class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def pascal(rowind):

            if rowind == 0:
                return [1]
            elif rowind == 1:
                return [1,1]
            else:
                temp = pascal(rowind-1)
                curr = [1]
                l = 0
                r = 1
                while r < len(temp):
                    curr.append(temp[l] + temp[r])
                    l += 1
                    r += 1
                curr.append(1)
                return curr
        return pascal(rowIndex)

        