class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, o = len(s1), len(s2), len(s3)
        
        if o == 0:
            if n or m: return False
            else: return True
        
        if n + m != o: return False

        if o == 1:
            if (s1 == s3 or s2 == s3): return True
            else: return False
        
        prev = set()
        if n and s1[0] == s3[0]: prev.add((1,0))
        if m and s2[0] == s3[0]: prev.add((0,1))

        i = 1
        while i < o:
            if len(prev) == 0:
                return False

            nxt = set()
            
            for a, b in prev:
                if a < n and s1[a] == s3[i]:
                    nxt.add((a + 1, b))
                if b < m and s2[b] == s3[i]:
                    nxt.add((a, b + 1))
            prev = nxt
            i += 1

        return (n, m) in prev            
