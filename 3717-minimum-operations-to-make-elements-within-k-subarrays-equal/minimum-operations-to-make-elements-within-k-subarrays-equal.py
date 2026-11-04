from typing import List

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, val):
        i += 1
        while i <= self.n:
            self.bit[i] += val
            i += i & -i

    def query(self, i):
        res = 0
        i += 1
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res

    def kth(self, k):
        idx = 0
        bit_mask = 1 << (self.n.bit_length() - 1)

        while bit_mask:
            nxt = idx + bit_mask
            if nxt <= self.n and self.bit[nxt] < k:
                idx = nxt
                k -= self.bit[nxt]
            bit_mask >>= 1

        return idx


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        vals = sorted(set(nums))
        size = len(vals)
        pos = {v: i for i, v in enumerate(vals)}

        count_tree = Fenwick(size)
        sum_tree = Fenwick(size)

        def update(v, delta):
            i = pos[v]
            count_tree.add(i, delta)
            sum_tree.add(i, v * delta)

        def window_cost():
            median_idx = count_tree.kth((x + 1) // 2)
            median = vals[median_idx]

            left_count = count_tree.query(median_idx)
            left_sum = sum_tree.query(median_idx)

            total_sum = sum_tree.query(size - 1)
            right_count = x - left_count
            right_sum = total_sum - left_sum

            return (median * left_count - left_sum +
                    right_sum - median * right_count)

        for i in range(x):
            update(nums[i], 1)

        costs = []

        for start in range(n - x + 1):
            costs.append(window_cost())

            if start + x < n:
                update(nums[start], -1)
                update(nums[start + x], 1)

        INF = float('inf')
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                curr[i] = curr[i - 1]

                if i >= x:
                    candidate = prev[i - x] + costs[i - x]
                    if candidate < curr[i]:
                        curr[i] = candidate

            prev = curr

        return prev[n]