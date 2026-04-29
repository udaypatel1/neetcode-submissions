from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        reference_counter = Counter(s1)

        left = 0
        right = len(s1)

        while right < len(s2) + 1:

            new_counter = Counter(s2[left:right])
            print(s2[left:right])

            if reference_counter == new_counter:
                return True
            
            left += 1
            right += 1

        return False







            
        