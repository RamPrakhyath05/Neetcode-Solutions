class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1
        sortFreq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        res = []
        for j in range(k):
            res.append(sortFreq[j][0])
        return res