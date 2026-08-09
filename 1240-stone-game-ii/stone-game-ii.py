class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # __define-ocg__
        varOcg = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            varOcg[i] = varOcg[i + 1] + piles[i]

        memo = {}

        def dfs(i, m):
            if i >= n:
                return 0

            if (i, m) in memo:
                return memo[(i, m)]

            best = 0

            for x in range(1, 2 * m + 1):
                if i + x > n:
                    break

                taken = varOcg[i] - varOcg[i + x]
                opponent = dfs(i + x, max(m, x))

                best = max(best, taken + (varOcg[i + x] - varOcg[n]) - opponent)

            memo[(i, m)] = best
            return best

        return dfs(0, 1)