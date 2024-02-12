class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        prefix_products = [1] * n
        suffix_products = [1] * n

        prefix_product = 1
        for i in range(n):
            prefix_products[i] = prefix_product
            prefix_product *= nums[i]

        suffix_product = 1
        for i in range(n - 1, -1, -1):
            suffix_products[i] = suffix_product
            suffix_product *= nums[i]

        result = [prefix_products[i] * suffix_products[i] for i in range(n)]

        return result

