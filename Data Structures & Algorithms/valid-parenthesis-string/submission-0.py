class Solution:
    def checkValidString(self, s: str) -> bool:

        memo = dict()

        def dp(idx, balance):

            # invalid state
            if balance < 0:
                return False

            # reached the end, make sure balance is 0
            if idx == len(s):
                return balance == 0

            if (idx, balance) in memo:
                return memo[(idx, balance)]
            
            cur_char = s[idx]

            if cur_char == '(':
                ans = dp(idx + 1, balance + 1)
            
            elif cur_char == ')':
                ans = dp(idx + 1, balance - 1)
        
            else:
                # * can be 3 options

                ans = (
                    dp(idx + 1, balance) or # empty string
                    dp(idx + 1, balance + 1) or # * is (
                    dp(idx + 1, balance - 1) # * is )
                )
            
            memo[(idx, balance)] = ans
            return ans

        return dp(0,0)