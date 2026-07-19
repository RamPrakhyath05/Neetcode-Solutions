class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix = []
        suffix = []
        prefProd = 1
        suffProd = 1
        for i in range(len(nums)):
            prefix.append(prefProd)
            prefProd = prefProd*nums[i]
            suffix.append(suffProd)
            suffProd = suffProd*nums[len(nums)-1-i]     
        suffix = suffix [::-1]
        for i in range(len(prefix)):
            output.append(prefix[i]*suffix[i])
        return output