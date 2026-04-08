from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return True if Counter(s).items() == Counter(t).items() else False

        
            
        