from collections import deque

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        '''
        its like a tree

        '34' -->

        (d) (e) (f)
        ||| ||| |||
        g,h,i g,h,i g,h,i

        etc

        # of root nodes is the AMOUNT of combos
        
        we want the actual combos

        can we DFS the whole tree and get every combo?
        is that efficient?
        '''

        if not digits:
            return []

        mapping = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno',
            '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        res = list()

        st = deque([(0, '')]) # index, cur_string

        while st:
            i, path = st.pop()

            # base case
            if i == len(digits):
                res.append(path)
                continue

            # push next states
            for ch in mapping[digits[i]]:
                st.append((i + 1, path + ch))

        return res


            
        