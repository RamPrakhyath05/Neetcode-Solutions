class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)
        startSeq = 0
        count = 0
        maxLen = 0
        for i in nums:
            if i-1 not in seq:
                startSeq = i
                count = 1
            while startSeq+1 in seq:
                startSeq += 1
                count += 1
            maxLen = max(maxLen, count)
        return maxLen


