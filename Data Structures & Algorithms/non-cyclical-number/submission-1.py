class Solution:
    def _sum_of_squared_digits(self, n: int) -> int:

        res = 0

        for d in str(n):
            res += int(d)**2

        return res

    def isHappy(self, n: int) -> bool:

        visited = set()

        val = self._sum_of_squared_digits(n)

        while val not in visited:

            visited.add(val)

            if val == 1:
                return True
            
            val = self._sum_of_squared_digits(val)
        
        return False
        


        