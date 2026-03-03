class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        state = [False] * (n + 1)
        state[0] = True

        for i in range(1, n + 1):
            for w in wordDict:
                size = len(w)
                if i >= size and s[i-size:i] in word_set and state[i-size]:
                    state[i] = True
                    break

        return state[n]