# This is Master's API interface.
# You should not implement it, or speculate about its implementation
class Master:
    def __init__(self, secret: str):
        self.secret = secret
        self.allowedGuesses = 10
        self.guessed = False

    def guess(self, word: str) -> int:
        if self.allowedGuesses == 0:
            return -1
        self.allowedGuesses -= 1
        count = 0
        for i in range(6):
            if word[i] == self.secret[i]:
                count += 1
        if count == 6:
            self.guessed = True
        return count


class Solution:
    def findSecretWord(self, words: list[str], master: Master) -> None:
        n = len(words)
        m = 6
        candidates = list(range(n))
        guessed = set()
        attempts = 0

        while candidates:
            nxt = self.get_best_next(words, candidates)
            guess = master.guess(words[nxt])
            guessed.add(nxt)
            attempts += 1
            if guess == 6: 
                return

            candidates = self.prune(words, nxt, guess, guessed)
    
    def get_best_next(self, words, candidates) -> int:
        """
        return next best possible candidate by counting char frequency and picking the one with higest freq chars
        """
        count = [[0] * 26 for _ in range(6)]
        for w in candidates:
            for i, char in enumerate(words[w]):
                count[i][ord(char) - ord('a')] += 1
        
        best_word = candidates[0]
        max_score = -1
        for w in candidates:
            score = sum(count[i][ord(char) - ord('a')] for i, char in enumerate(words[w]))
            if score > max_score:
                max_score = score
                best_word = w
        return best_word

    def prune(self, words: list[str], nxt: int, guess: int, guessed: set[int]) -> list[int]:
        """
        prune 'words' of all the words that do not have exactly 'guess' characters in common with nxt 
        this is because if they have more or less in common they mathematically can't have enogh char equal to the secret
        """
        n = len(words)
        new_candidates = []
        for x in range(n):
            if nxt != x and x not in guessed:
                common = 0
                for i in range(6):
                    if words[nxt][i] == words[x][i]: common += 1
                if common == guess:
                    new_candidates.append(x)
                else: guessed.add(x)
        return new_candidates