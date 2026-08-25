class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [dict() for _ in range(n)]
        ans = 0

        for i in range(n):
            for j in range(i):
                d = nums[i] - nums[j]

                prev = dp[j].get(d, 0)
                dp[i][d] = dp[i].get(d, 0) + prev + 1

                ans += prev

        return ans