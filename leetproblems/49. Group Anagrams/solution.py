class Solution:
    COUNTSET = [0] * 26
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = []
        encoding_to_groupidx = {}

        for s in strs:
            encoding = self.encodeString(s)

            if encoding in encoding_to_groupidx:
                res[encoding_to_groupidx[encoding]].append(s)
            else:
                encoding_to_groupidx[encoding] = len(res)
                res.append([s])

        return res
            
    def encodeString(self, s: str) -> int:
        encoding = self.COUNTSET.copy()
        for c in s:
            idx = ord(c) - ord('a')
            encoding[idx] += 1
        return tuple(encoding)