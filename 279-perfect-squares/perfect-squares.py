class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [float("inf")] * n

        for target in range(1, n + 1):
            square = 1

            while square * square <= target:
                dp[target] = min(dp[target], dp[target - square * square] + 1)
                square += 1

        return dp[n]