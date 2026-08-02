class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = 0
        p2 = 0
        seen = set()
        maxLen = 0
        while p2 < len(s):
            while s[p2] in seen:
                seen.remove(s[p1])
                p1+=1
            if s[p2] not in seen:
                seen.add(s[p2])
            p2+=1
            maxLen = max(maxLen, len(seen))
        return maxLen
        
