class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        MAXX = 2048
        present = [False] * MAXX
        for x in nums:
            present[x] = True

        dp = [[False] * MAXX for _ in range(4)]
        dp[0][0] = True

        values = [i for i, ok in enumerate(present) if ok]

        for k in range(3):
            for x in range(MAXX):
                if dp[k][x]:
                    for v in values:
                        dp[k + 1][x ^ v] = True

        return sum(dp[3])