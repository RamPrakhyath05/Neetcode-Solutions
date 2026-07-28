class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
        return max(freq,key=freq.get)