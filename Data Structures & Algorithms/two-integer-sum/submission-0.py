class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for i in range(len(nums)):
            if target - nums[i] not in numbers:
                numbers[nums[i]] = i
            else:
                return [numbers[target-nums[i]],i]
        return []