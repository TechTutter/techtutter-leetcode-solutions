class Solution:
    """
    seen_numbers = set()
    while True:
        n = sum of squares of digits of n
        if n == 1: return True
        if n in seen_numbers: return False
        seen_numbers.add(n)
    """
    def isHappy(self, n: int) -> bool:
        found = set()
        curr_sum = n
        
        while True:
            s = str(curr_sum)
            curr_sum = 0
            for c in s:
                digit = int(c)
                curr_sum += digit ** 2
            
            if curr_sum == 1:
                return True
            elif curr_sum in found:
                return False
            else:
                found.add(curr_sum)