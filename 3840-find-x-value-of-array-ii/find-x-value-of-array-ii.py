class Solution:
    def resultArray(self, nums: list[int], k: int, queries: list[list[int]]) -> list[int]:
        n = len(nums)
        size = 1
        while size < n:
            size <<= 1

        # (product of segment, counts of prefix products)
        tree = [(1 % k, [0] * k) for _ in range(2 * size)]

        def make_node(v):
            v %= k
            cnt = [0] * k
            cnt[v] = 1
            return v, cnt

        def merge(a, b):
            pa, ca = a
            pb, cb = b
            cnt = ca[:]

            for r in range(k):
                if cb[r]:
                    cnt[(pa * r) % k] += cb[r]

            return (pa * pb) % k, cnt

        for i, v in enumerate(nums):
            tree[size + i] = make_node(v)

        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[i << 1], tree[i << 1 | 1])

        def update(pos, value):
            p = size + pos
            tree[p] = make_node(value)

            p >>= 1
            while p:
                tree[p] = merge(tree[p << 1], tree[p << 1 | 1])
                p >>= 1

        def query(l, r):
            left = None
            right = None

            l += size
            r += size + 1

            while l < r:
                if l & 1:
                    left = tree[l] if left is None else merge(left, tree[l])
                    l += 1

                if r & 1:
                    r -= 1
                    right = tree[r] if right is None else merge(tree[r], right)

                l >>= 1
                r >>= 1

            if left is None:
                return right
            if right is None:
                return left
            return merge(left, right)

        result = []

        for index, value, start, x in queries:
            update(index, value)
            result.append(query(start, n - 1)[1][x])

        return result