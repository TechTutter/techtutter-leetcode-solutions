from collections import Counter

class Solution:

    def findSubstring(self,s, words):
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = Counter(words)
        result = []

        for i in range(word_len):  # shift della finestra per coprire tutti gli offset
            left = i
            right = i
            curr_count = Counter()
            
            while right + word_len <= len(s):
                word = s[right:right+word_len]
                right += word_len
                if word in word_count:
                    curr_count[word] += 1
                    # se ci sono troppe occorrenze, sposta il left
                    while curr_count[word] > word_count[word]:
                        left_word = s[left:left+word_len]
                        curr_count[left_word] -= 1
                        left += word_len
                    # se la finestra ha tutte le parole
                    if right - left == total_len:
                        result.append(left)
                else:
                    # parola non valida, reset
                    curr_count.clear()
                    left = right
        return result