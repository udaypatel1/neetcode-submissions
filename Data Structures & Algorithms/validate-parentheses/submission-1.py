from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:

        if not s:
            return False
        
        if len(s) == 1:
            return False

        m = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        st = deque([])

        for c in s:

            if m.get(c) is not None:
                st.append(c)
            else:
                # closed paren
                if st and m.get(st[-1]) == c:
                    # successful pair, pop it
                    st.pop()
                else:
                    return False
        
        return True if not st else False

        
        