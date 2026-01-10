class Solution:
    """
    map_st = {}, map_ts = {}
    for char_s, char_t in zip(s, t):
        if char_s in map_st and map_st[char_s] != char_t: return False
        if char_t in map_ts and map_ts[char_t] != char_s: return False
        map_st[char_s] = char_t
        map_ts[char_t] = char_s
    return True
    """
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_st = {}
        map_ts = {}

        # zip e.g. ["foo", "bar"] -> [("f", "b"), ("o", "a"), ("o", "r")]
        for a, b in zip(s, t):
            if a in map_st and map_st[a] != b:
                return False
            if b in map_ts and map_ts[b] != a:
                return False

            map_st[a] = b
            map_ts[b] = a

        return True