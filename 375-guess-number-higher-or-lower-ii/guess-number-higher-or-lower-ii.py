from functools import cache

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @cache
        def dp(l, r):
            if l >= r:
                return 0

            ans = float('inf')
            for x in range(l, r + 1):
                ans = min(ans, x + max(dp(l, x - 1), dp(x + 1, r)))
            return ans

        return dp(1, n)