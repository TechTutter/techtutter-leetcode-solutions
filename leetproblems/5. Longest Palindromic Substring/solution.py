from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        best_start = best_end = 0

        for x in range(1, n):
            i = j = x
            odd_center = (x, x)
            even_center = (x-1, x)

            for i, j in [odd_center, even_center]:
                while i >= 0 and j < n:
                    if s[i] != s[j]:
                        break
                    i -= 1
                    j += 1
                i += 1
                j -= 1

                # Adjust result if needed
                size = j - i
                curr_best_size = best_end - best_start
                if size >= curr_best_size:
                    best_start = i
                    best_end = j 

        return s[best_start:best_end+1]

    def longestPalindrome2(self, s: str) -> str:
        '''
        O(n^3) somewhat acceptable with n <= 1000
        '''
        n = len(s)
        if n < 2:
            return s

        start = end = 0

        char_to_index_map = defaultdict(list)
        for i in range(n):
            char_to_index_map[s[i]].append(i)

        for curr_start in range(n):
            end_candidates = char_to_index_map[s[curr_start]]
            for x in range(len(end_candidates) -1, -1, -1):
                curr_end = end_candidates[x]
                size = curr_end - curr_start
                curr_best_size = end - start
                if size < curr_best_size:
                    break

                i, j = curr_start, curr_end

                while i < j:
                    if s[i] != s[j]:
                        break
                    i += 1
                    j -= 1
                if i == j or i > j and s[i] == s[j]:
                    start = curr_start
                    end = curr_end

        return s[start:end+1]