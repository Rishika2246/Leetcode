from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + [x for x in nums if x != 0] + [1]
        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        # length = gap between left and right boundary balloons
        for length in range(2, n):
            for left in range(n - length):
                right = left + length

                for last in range(left + 1, right):
                    coins = (
                        nums[left] * nums[last] * nums[right]
                        + dp[left][last]
                        + dp[last][right]
                    )
                    dp[left][right] = max(dp[left][right], coins)

        return dp[0][n - 1]