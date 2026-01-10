class Solution:        
    """
    for each digit in the number:
        calculate its weight (place value)
        if digit is 4:
            append Roman form for 4 at that weight
        else if digit is 9:
            append Roman form for 9 at that weight
        else if digit <= 3:
            append base symbol times digit
        else if digit >= 5:
            append '5' symbol + (digit - 5) symbol
    """
    DIGIT_WEIGHT_TO_ROMAN = {
        0: ["I", "V"],
        1: ["X", "L"],
        2: ["C", "D"],
        3: ["M"]
    }

    DIGIT_WEIGHT_TO_ROMAN_SUBTRACTORS = {
        0: ["IV", "IX"],
        1: ["XL", "XC"],
        2: ["CD", "CM"]
    }
    
    def intToRoman(self, num: int) -> str:
        val = str(num)
        size = len(val)
        roman = ""
        
        for i, c in enumerate(val):
            curr = int(c)
            weight = size - i - 1
            
            if curr == 4:
                roman += self.DIGIT_WEIGHT_TO_ROMAN_SUBTRACTORS.get(weight)[0]
            elif curr == 9:
                roman += self.DIGIT_WEIGHT_TO_ROMAN_SUBTRACTORS.get(weight)[1]
            elif curr <= 3:
                roman += self.DIGIT_WEIGHT_TO_ROMAN.get(weight)[0] * curr
            elif curr >= 5:
                roman += self.DIGIT_WEIGHT_TO_ROMAN.get(weight)[1] + self.DIGIT_WEIGHT_TO_ROMAN.get(weight)[0] * (curr - 5)
        
        return roman