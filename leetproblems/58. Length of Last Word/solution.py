class Solution:
    """
    count all alphabetic chars starting from the end
    if the count is 0 and a non-alphabetic char is found, return count
    """
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == " " or not s[i].isalpha():
                if res != 0: return res
            else:
                res += 1
        return res