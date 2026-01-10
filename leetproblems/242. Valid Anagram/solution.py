class Solution:
    """
    if length(s) != length(t): return False
    counts = {}
    for char_s, char_t in zip(s, t):
        counts[char_s] = counts.get(char_s, 0) - 1
        counts[char_t] = counts.get(char_t, 0) + 1
    return all counts are zero
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # bitvector, +1 for occurrencies of first, -1 for the other
        occurrencies = {}
        for a, b in zip(s, t):
            occurrencies[a] = occurrencies.get(a, 0) - 1
            occurrencies[b] = occurrencies.get(b, 0) + 1
            
        have_same_characters_frequency = all(val == 0 for val in occurrencies.values())
        return have_same_characters_frequency