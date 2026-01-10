class Solution:
    """
    p_s = 0, p_t = 0
    while p_s < len(s) and p_t < len(t):
        if s[p_s] == t[p_t]:
            p_s++
        p_t++
    return p_s == len(s)
    """
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        if len(s) == 0:
            return True

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
            
        return i == len(s)
