import re


class Solution:
    """
    cleaned = remove non-alphanumeric and lowercase s
    n = length of cleaned
    left = 0, right = n - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left++, right--
    return True
    """
    def isPalindrome(self, s: str) -> bool:

        cleaned = re.sub("[^a-zA-Z0-9]", "", s).lower()
        n = len(cleaned)
        i = 0
        j = n - 1

        if n <= 0:
            return True

        while i < j:
            if cleaned[i] != cleaned[j]:
                return False
            else:
                i += 1
                j -= 1

        return True
