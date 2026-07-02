class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res=[]
        c = 0
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]]=1
            else:
                freq[nums[i]]+=1
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        while c<k:
            res.append(sorted_freq[c][0])
            c+=1
        return res

