class Solution:
    """
    s = s.strip()
    length = 0
    for i from len(s)-1 down to 0:
        if s[i] == ' ': break
        length++
    return length
    """
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        l = len(s)
        for i in range(l - 1, -1, -1):
            if s[i] == " ":
                return l - i - 1
        return l