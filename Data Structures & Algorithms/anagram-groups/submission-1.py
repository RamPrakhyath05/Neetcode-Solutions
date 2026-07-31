class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for i in strs:
            chars = tuple(sorted(list(i)))
            if chars not in words:
                words[chars] = [i]
            else:
                words[chars].append(i)
        return list(words.values())