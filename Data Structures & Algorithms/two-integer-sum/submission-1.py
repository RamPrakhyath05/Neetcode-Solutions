class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for i in range(len(nums)):
            toFind = target - nums[i]
            if toFind not in numbers:
                numbers[nums[i]] = i
            else:
                return [numbers[toFind],i]
        return []