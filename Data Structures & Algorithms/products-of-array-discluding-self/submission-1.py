class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        prefix = 1
        res = [1] * l
        for i in range(l):
            res[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for j in range(l):
            res[l-j-1] *= suffix
            suffix *= nums[l-j-1]
        return res