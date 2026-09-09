class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        seen1 = {}
        seen2 = {}
        count = 0

        for letter in s:
            if letter not in seen1:
                seen1[letter] = 0
            else:
                seen1[letter] += 1

        for letter in t:
            if letter not in seen2:
                seen2[letter] = 0
            else:
                seen2[letter] += 1

        for key in seen1:
            if len(seen1) != len(seen2) or key not in seen2 or seen1[key] != seen2[key]:
                return False
        
        return True
             
        