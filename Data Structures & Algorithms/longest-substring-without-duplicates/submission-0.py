class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest = 0

        l = 0
        r = 0
        while l < len(s):

            seen = set()

            while r < len(s) and s[r] not in seen:
                seen.add(s[r])
                r += 1

            longest = max(longest, r - l)

            l += 1
            r = l

        return longest
            




        