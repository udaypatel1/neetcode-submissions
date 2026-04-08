class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned_string = ''.join(c.lower() for c in s if c.isalnum())

        l = 0
        r = len(cleaned_string) - 1

        while l < r:

            if cleaned_string[l] != cleaned_string[r]:
                return False
            
            l += 1
            r -= 1
        
        return True

