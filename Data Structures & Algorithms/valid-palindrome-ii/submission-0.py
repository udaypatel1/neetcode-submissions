
class Solution:
    def validPalindrome(self, s: str) -> bool:

        if s == s[::-1]:
            return True

        for ptr, c in enumerate(s):

            if ptr + 1 < len(s):

                modified = s[0:ptr] + s[ptr + 1:]

                if modified == modified[::-1]:
                    return True
        
        return False

        
        