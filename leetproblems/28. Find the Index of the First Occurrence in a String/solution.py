class Solution:
    """
    n, m = lengths of haystack and needle
    for i from 0 to n - m:
        if haystack[i...i+m] == needle:
            return i
    return -1
    """
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        
        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i
                
        return -1
