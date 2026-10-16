class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        size = 4 * n
        tree = [0] * size
        lazy = [0] * size
        ans = 0

        def apply(node, start, end, val):
            length = end - start + 1
            tree[node] = (tree[node] + 2 * val * sum_distinct[node] + val * val * length) % MOD
            sum_distinct[node] = (sum_distinct[node] + val * length) % MOD
            lazy[node] += val

        sum_distinct = [0] * size

        def push(node, start, end):
            if lazy[node] == 0 or start == end:
                return
            mid = (start + end) // 2
            val = lazy[node]
            apply(node * 2, start, mid, val)
            apply(node * 2 + 1, mid + 1, end, val)
            lazy[node] = 0

        def update(node, start, end, left, right):
            if left <= start and end <= right:
                apply(node, start, end, 1)
                return

            push(node, start, end)
            mid = (start + end) // 2

            if left <= mid:
                update(node * 2, start, mid, left, right)
            if right > mid:
                update(node * 2 + 1, mid + 1, end, left, right)

            tree[node] = (tree[node * 2] + tree[node * 2 + 1]) % MOD
            sum_distinct[node] = (
                sum_distinct[node * 2] + sum_distinct[node * 2 + 1]
            ) % MOD

        last = {}

        for i, x in enumerate(nums):
            prev = last.get(x, -1)
            update(1, 0, n - 1, prev + 1, i)
            ans = (ans + tree[1]) % MOD
            last[x] = i

        return ans