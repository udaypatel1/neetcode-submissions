from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return True if frozenset(Counter(s).items()) == frozenset(Counter(t).items()) else False

        
            
        