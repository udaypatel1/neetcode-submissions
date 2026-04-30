class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        count = 0

        # center expansion

        def expand(left, right):
            nonlocal count

            # boundary check and if both chars are equal
            while left >= 0 and right < n and s[left] == s[right]:

                count += 1
                left -= 1
                right += 1

        for i in range(n):
            expand(i, i)
            expand(i, i+1)

        return count