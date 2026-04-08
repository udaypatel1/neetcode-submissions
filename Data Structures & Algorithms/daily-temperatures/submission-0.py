from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        LEN = len(temperatures)
        result = [0] * LEN

        stack = deque()

        for idx, temp in enumerate(temperatures):

            # print(stack)

            if not stack:
                stack.append((idx, temp))
                continue
            
            '''
            cur temp is now greater than top of stack
            we need to stabilize the stack
            '''

            while stack and temp > stack[-1][1]:
                
                peek_idx, peek_temp = stack.pop()

                result[peek_idx] = idx - peek_idx

            stack.append((idx, temp))

        return result

        





        