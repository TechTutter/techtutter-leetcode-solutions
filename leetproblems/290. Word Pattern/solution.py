class Solution:
    """
    words = s.split()
    if length(pattern) != length(words): return False
    char_to_word = {}, word_to_char = {}
    for char, word in zip(pattern, words):
        if char already mapped and mapped_word != word: return False
        if word already mapped and mapped_char != char: return False
        char_to_word[char] = word
        word_to_char[word] = char
    return True
    """
    def wordPattern(self, pattern: str, s: str) -> bool:
        used = set()
        char_to_word_map = dict()

        word_list = s.split()
        chars = len(pattern)
        words = len(word_list)

        if(chars != words):
            return False

        for i in range(chars):
            mapped = char_to_word_map.get(pattern[i])

            if(mapped and mapped != word_list[i]):
                return False
            elif(not mapped):
                if (word_list[i] in used):
                    return False
                else:
                    used.add(word_list[i])
                    char_to_word_map[pattern[i]] = word_list[i]
        
        return True