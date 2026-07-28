class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)
        curLen = 0
        seqStart = 0
        maxLen = 0
        for i in seq:
            if i-1 not in seq:
                seqStart = i
                curLen = 1
            while seqStart+1 in seq:
                seqStart += 1
                curLen += 1
            maxLen = max(maxLen, curLen)
        return maxLen