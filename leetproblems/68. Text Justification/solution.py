class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []

        current_line = []
        current_line_size = 0
        current_line_available_space = maxWidth

        for w in words:
            if current_line_available_space - len(w) < 0:
                self.justify_line(maxWidth, current_line_size, current_line, res)
                current_line.clear()
                current_line_size = 0
                current_line_available_space = maxWidth

            current_line.append(w)
            current_line.append("") # placeholder for spaces
            current_line_size += len(w)
            current_line_available_space -= len(w) + 1
        
        if current_line:
            del current_line[len(current_line)-1]
            current_line_available_space += 1
            for i in range(1, len(current_line) - 1, 2):
                current_line[i] = " "
            current_line.append(" " *current_line_available_space)
            res.append("".join(current_line))
        
        return res
                
    def justify_line(self, max_width, current_line_size, current_line, output):
        words = len(current_line) // 2
        spaces_needed = max_width - current_line_size
        spaces_count = max(words - 1, 1)
        spaces_per_word_count = spaces_needed // spaces_count
        overflowing_spaces_count = spaces_needed % spaces_count
        
        space = " " * spaces_per_word_count
        overflowing_space = " " * (spaces_per_word_count + 1) 
        
        for i in range(1, max(len(current_line)-1, 2), 2):
            if overflowing_spaces_count > 0:
                current_line[i] = overflowing_space
                overflowing_spaces_count -= 1
                
            else:
                current_line[i] = space
                
        output.append("".join(current_line))
        
s = Solution()
print(s.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))


"""
currentLine = []
for w in words:
    if currentLine + w does not fit in available_space -> justify current line
    else currentLine.append(w)

if len(currentLine) -> append to res last words to cleanup

-- def justify_current_line:
spaces_needed = maxWidth - len(all words in currentLine)
divider = max(len(currentLine) - 1, 1)
spaces_per_word = spaces_needed // divider
overflowing_spaces = spaces_needed % divider
"""
        