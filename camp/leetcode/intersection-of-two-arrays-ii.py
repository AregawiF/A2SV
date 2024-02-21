class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for l in range(len(nums1)):
            r = 0
            while r < len(nums2):
                if nums1[l] == nums2[r]:
                    ans.append(nums2[r])
                    nums2.remove(nums2[r])
                    break
                r += 1
        return ans
                