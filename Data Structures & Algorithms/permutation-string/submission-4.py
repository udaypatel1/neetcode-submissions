from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        reference_counter = Counter(s1)

        left = 0
        right = len(s1)

        cur_counter = Counter(s2[left:right])

        while right < len(s2) + 1:

            if reference_counter == cur_counter:
                return True

            # decrement or remove "outbound" char
            if cur_counter.get(s2[left]) == 1:
                del cur_counter[s2[left]]
            else:
                cur_counter[s2[left]] -= 1

            # increment or add new "incoming" char

            # bounds check for new char
            if right + 1 < len(s2) + 1:

                # if new char doesnt exist in dict, add it with 1
                if cur_counter.get(s2[right]) is None:
                    cur_counter[s2[right]] = 1
                else:
                    # otherwise increment that if it already exists
                    cur_counter[s2[right]] += 1
            
            else:
                # early break if the next is the last
                break
            
            left += 1
            right += 1

        return False







            
        