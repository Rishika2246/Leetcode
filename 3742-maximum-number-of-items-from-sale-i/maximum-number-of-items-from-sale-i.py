from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        mn = min(p for _, p in items)
        dp = [0] * (budget + 1)

        for f, p in items:
            cnt = sum(g % f == 0 for g, _ in items)
            for b in range(budget, p - 1, -1):
                dp[b] = max(dp[b], dp[b - p] + cnt)

        return max(dp[b] + (budget - b) // mn for b in range(budget + 1))