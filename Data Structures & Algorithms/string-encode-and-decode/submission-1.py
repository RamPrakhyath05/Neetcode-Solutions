class Solution:
    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            l = len(strs[i])
            strs[i] = str(l) + '#' + strs[i]
        encoded = ''.join(strs)
        return encoded

    def decode(self, s: str) -> List[str]:
        i=0
        res = []
        while i<len(s):
            j = i
            length = ""
            while s[j] != "#":
                length += s[j]
                j += 1
            j += 1
            strCount = 0
            l = int(length)
            string = ""
            while strCount < l:
                string += s[j]
                j+=1
                strCount += 1
            res.append(string)
            i=j
        return res
        