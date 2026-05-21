from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        r = Counter(ransomNote)
        m = Counter(magazine)

        return True if not (r - m) else False

        