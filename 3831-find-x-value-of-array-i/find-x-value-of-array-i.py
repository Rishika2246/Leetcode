class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        ans = [0] * k
        dp = [0] * k

        for x in nums:
            x %= k
            ndp = [0] * k

            ndp[x] += 1

            for r in range(k):
                if dp[r]:
                    ndp[(r * x) % k] += dp[r]

            for r in range(k):
                ans[r] += ndp[r]

            dp = ndp

        return ans