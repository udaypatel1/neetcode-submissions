class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        '''
        see how many cars will 'pile up' together before reaching target
        at time target, count up the total in the monotonic stack, which are all fleeted (joined) cars
        '''

        cars = sorted(zip(position, speed), reverse=True)

        completion_stack = []

        for pos, spd in cars:
            
            time_when_reached = (target - pos) / spd

            if completion_stack and time_when_reached <= completion_stack[-1]:

                continue
            else:
                completion_stack.append(time_when_reached)
        
        return len(completion_stack)

        