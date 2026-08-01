class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            length = ""
            while s[j] != "#":
                length += s[j]
                j += 1
            j += 1
            l = int(length)
            string = s[j:j+l]
            j += l
            res.append(string)
            i = j
        return res
        