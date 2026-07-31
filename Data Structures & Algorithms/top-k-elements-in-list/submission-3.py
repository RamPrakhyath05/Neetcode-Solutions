class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        freq = list(seen.items())
        res = []
        c = 0
        while c < k:
            mx = max(freq,key = lambda x : x[1])
            res.append(mx[0])
            freq.remove(mx)
            c+=1
        return res
        