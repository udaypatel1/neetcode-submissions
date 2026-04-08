class Solution:
    def scoreOfString(self, s: str) -> int:

        r_sum = 0

        for c in range(len(s) - 1):

            first = ord(s[c])
            second = ord(s[c + 1])

            r_sum += abs(first - second)
        
        return r_sum



        