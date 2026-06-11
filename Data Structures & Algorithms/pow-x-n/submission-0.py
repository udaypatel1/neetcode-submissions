class Solution:
    def myPow(self, x: float, n: int) -> float:

        result = 1

        for _ in range(abs(n)):

            if n < 0:
                result *= (1 / x)
            else:
                result *= x
            
        return result



        