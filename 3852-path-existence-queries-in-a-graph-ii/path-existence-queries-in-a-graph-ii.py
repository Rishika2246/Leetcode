from bisect import bisect_right

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        order = sorted((num, i) for i, num in enumerate(nums))
        vals = [x[0] for x in order]
        pos = [0] * n

        for i, (_, node) in enumerate(order):
            pos[node] = i

        nxt = [0] * n
        r = 0
        for l in range(n):
            r = max(r, l)
            while r + 1 < n and vals[r + 1] - vals[l] <= maxDiff:
                r += 1
            nxt[l] = r

        LOG = n.bit_length()
        up = [nxt]

        for _ in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n)])

        ans = []

        for u, v in queries:
            if u == v:
                ans.append(0)
                continue

            left, right = pos[u], pos[v]
            if left > right:
                left, right = right, left

            jumps = 0
            cur = left

            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < right:
                    cur = up[k][cur]
                    jumps += 1 << k

            ans.append(jumps + 1 if nxt[cur] >= right else -1)

        return ans