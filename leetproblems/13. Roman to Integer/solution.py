class Solution:
    """
    result = 0
    pointer = 0
    while pointer < length(s) - 1:
        if current character can be a subtractor (I, X, C) AND next character is a larger value:
            result += special subtractive value
            pointer += 2
        else:
            result += normal value
            pointer += 1
    if one character remains:
        result += normal value
    return result
    """
    ROMAN_TO_INTEGER_MAP = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    SUBTRACTED_MAP = {
        "V": 4,
        "X": 9,
        "L": 40,
        "C": 90,
        "D": 400,
        "M": 900
    }
    
    def romanToInt(self, s: str) -> int:
        result = 0
        i = 0

        while(i < len(s) - 1):
            if(s[i] == "I" or s[i] == "X" or s[i] == "C"):
                if(s[i+1] in self.SUBTRACTED_MAP and self.ROMAN_TO_INTEGER_MAP.get(s[i]) < self.ROMAN_TO_INTEGER_MAP.get(s[i+1])):
                    result += self.SUBTRACTED_MAP.get(s[i+1]) 
                    i += 2
                    continue
                
            result += self.ROMAN_TO_INTEGER_MAP.get(s[i])
            i += 1
        
        if(i == len(s) - 1):
            result += self.ROMAN_TO_INTEGER_MAP.get(s[i])

        return result