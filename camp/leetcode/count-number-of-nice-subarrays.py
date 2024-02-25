class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        right = 0
        odds = 0
        ans = 0

        while right < n:
            if nums[right] % 2 == 1:
                odds += 1
            
            while odds == k:
                temp = right + 1
                while temp < n and nums[temp] % 2 == 0:
                    temp += 1
                right_even_count = temp - right
                left_even_count = 0
                while nums[left] % 2 == 0:
                    left_even_count += 1
                    left += 1
                ans += (left_even_count + 1) * right_even_count
                left += 1
                odds -= 1

            right += 1

        return ans