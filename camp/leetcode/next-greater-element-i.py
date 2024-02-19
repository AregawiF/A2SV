class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = [0]
        ans = [-1] * len(nums2)
        result = []
        for i in range(1,len(nums2)):
            while stack and (nums2[i] > nums2[stack[-1]]):
                ans[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(i)
        for n in nums1:
            ind = nums2.index(n)
            result.append(ans[ind])
        
        return result
