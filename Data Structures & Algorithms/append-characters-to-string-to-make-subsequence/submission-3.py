class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        ptr_t = 0

        for ch in s:

            if ptr_t < len(t) and ch == t[ptr_t]:
                ptr_t += 1

        return len(t) - ptr_t