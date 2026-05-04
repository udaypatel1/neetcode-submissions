from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        if '0000' in deadends:
            return -1

        q = deque([('0000', 0)])

        visited = set()
        visited.add('0000')

        while q:

            state, moves = q.popleft()

            if state == target:
                return moves

            # 8 children
            # generate 8 neighbors
            for digit in range(4):

                cur_digit = int(state[digit])

                for d_scroll in [-1, 1]:

                    new_digit = (cur_digit + d_scroll) % 10
                    new_state = state[:digit] + str(new_digit) + state[digit+1:]

                    if new_state not in deadends and new_state not in visited:
                        visited.add(new_state)
                        q.append((new_state, moves + 1))
        
        return -1

                

        

        