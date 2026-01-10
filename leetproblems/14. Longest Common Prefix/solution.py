class Solution:
    """
    prefix = ""
    while not done:
        for each string in strs:
            if string length <= index:
                done
            if current_char is None:
                current_char = string[index]
            else if current_char != string[index]:
                done
        if not done:
            prefix += current_char
            index++
    return prefix
    """
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        done = False
        
        idx = 0
        curr_character = None
        
        while not done:
            for w in strs:
                # if any of the strings is over, break the loop
                if len(w) <= idx:
                    done = True
                    break
                
                # initialize curr_char first time, then compare it word by word
                if curr_character == None:
                    curr_character = w[idx]
                    
                elif curr_character != w[idx]:
                    done = True
                    break
            if not done:
                prefix = prefix + curr_character    
                curr_character = None
                idx = idx + 1
            
        return prefix