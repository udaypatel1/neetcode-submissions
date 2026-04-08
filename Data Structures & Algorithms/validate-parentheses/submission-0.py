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
        

        st = []

        for char in s:

            if char in m:
                st.append(char)
            elif st:
                popped_node = st.pop(-1)
                if m.get(popped_node) != char:
                    return False
            else:
                return False
                
        return True if len(st) == 0 else False
                


        