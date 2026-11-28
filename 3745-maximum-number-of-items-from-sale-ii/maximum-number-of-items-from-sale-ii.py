from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        freq = [0] * (n + 1)
        min_price = float('inf')

        for f, p in items:
            freq[f] += 1
            min_price = min(min_price, p)

        gain = [0] * (n + 1)

        for f in range(1, n + 1):
            if freq[f]:
                total = sum(freq[m] for m in range(f, n + 1, f))
                gain[f] = total - 1

        deals = []
        for f, p in items:
            if gain[f] > 0 and p < 2 * min_price:
                deals.append((p, gain[f]))

        deals.sort()

        ans = 0
        for price, count in deals:
            take = min(count, budget // price)
            ans += 2 * take
            budget -= take * price

            if take < count:
                break

        ans += budget // min_price
        return ans