class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(nums, reverse=True)
        seen = {}
        for i in nums:
            seen[i] = seen.get(i,0) + 1
        print(seen)
        