class Solution:
    """
    left = 0, max_len = 0
    seen = {} # char -> index
    for right, char in enumerate(s):
        if char in seen:
            left = max(left, seen[char] + 1)
        seen[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        l = 0
        unique_chars = {}
        
        for r, right in enumerate(s):      
            idx = unique_chars.get(right)
            unique_chars[right] = r
            
            if idx != None:
                l = max(l, idx + 1)

            curr_count = r - l + 1
            if max_count < curr_count:
                max_count = curr_count
        return max_count

