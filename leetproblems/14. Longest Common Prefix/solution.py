class Solution:
    """
    if the end of a string is reached, return current prefixes
    else if a different character is found for index i, return prefixes
    else simply append the character to prefix list and continue
    """
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = []
        
        i = 0
        while True:
            c = ''
            for s in strs:
                if i == len(s):
                    return ''.join(prefix)
                if not c:
                    c = s[i]
                elif c != s[i]:
                    return ''.join(prefix)
            prefix.append(c)
            i += 1
