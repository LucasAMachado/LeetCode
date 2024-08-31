from typing import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool: 
        noteCounter : dict = Counter(ransomNote)
        magazineCounter : dict = Counter(magazine)

        for char, count in noteCounter.items():
            # The counter will return 0 if the the key in not in the dict
            # checks if the count in the magazine for a given char is less than the count 
            # of that same char in the note
            if magazineCounter[char] < count:
                return False
            
        return True