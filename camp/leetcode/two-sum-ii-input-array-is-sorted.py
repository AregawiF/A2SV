class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # left = 0
        # # right = 0
        # ans = []
        # for left in range(len(numbers)):
        #     for r in range(left+1,len(numbers)):
        #         if numbers[left] + numbers[r] == target:
        #             ans = [left+1, r+1]
        #             break

        left = 0
        right = len(numbers) -1
        while left < right :
            if (numbers[left] + numbers[right] > target) :
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left+1, right+1]

        return []