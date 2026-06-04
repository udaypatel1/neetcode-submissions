from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operators = {
            '*',
            '+',
            '-',
            '/'
        }

        st = deque()

        for token in tokens:

            print(st)

            if token in operators:
                # pop last two, perform operator, store result

                second = int(st.pop())
                first = int(st.pop())

                result = None

                if token == '+':
                    result = first + second
                elif token == '-':
                    result = first - second
                elif token == '*':
                    result = first * second
                elif token == '/':
                    result = int(first / second)
                
                st.append(str(result))
            
            else:
                st.append(token)
        
        return int(st[-1])