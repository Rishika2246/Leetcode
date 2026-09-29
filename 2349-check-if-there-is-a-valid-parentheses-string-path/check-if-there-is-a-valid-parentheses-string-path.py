class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        if grid[0][0] == ')':
            return False

        length = m + n - 1
        if length % 2:
            return False

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 << 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                mask = 0
                if i:
                    mask |= dp[i - 1][j]
                if j:
                    mask |= dp[i][j - 1]

                if grid[i][j] == '(':
                    mask <<= 1
                else:
                    mask >>= 1

                remaining = (m - 1 - i) + (n - 1 - j)

                if remaining + 1 < mask.bit_length():
                    mask &= (1 << (remaining + 1)) - 1

                dp[i][j] = mask

        return bool(dp[m - 1][n - 1] & 1)