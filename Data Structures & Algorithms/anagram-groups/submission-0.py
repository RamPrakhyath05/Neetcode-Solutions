class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashTable={}
        for s in strs:
            splitStr = tuple(sorted(s))
            if splitStr not in hashTable:
                hashTable[splitStr] = [s]
            else:
                hashTable[splitStr].append(s)
        return list(hashTable.values())
