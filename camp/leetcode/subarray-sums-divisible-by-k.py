# class Solution:
#     def subarraysDivByK(self, nums: List[int], k: int) -> int:
#         right = 0
#         count = 0
#         s = sum(nums)
#         if s % k == 0:
#             count += 1
#         prefix = [0, nums[0]]
#         for idx in range(1,len(nums)):
#             prefix.append( prefix[-1] + nums[idx])

#         for left in range(len(nums)):
#             currsum = s - prefix[left]
#             if currsum % k ==0:
#                 count += 1
#             for right in range(len(nums)-1, left, -1):
#                 currsum -= nums[right]
#                 if currsum % k ==0:
#                     count += 1

#         return count
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        remainder_count = {0: 1}  
        curr_sum = 0

        for num in nums:
            curr_sum += num
            remainder = curr_sum % k
            remainder = (remainder + k) % k
            if remainder in remainder_count:
                count += remainder_count[remainder]
            remainder_count[remainder] = remainder_count.get(remainder, 0) + 1

        return count
