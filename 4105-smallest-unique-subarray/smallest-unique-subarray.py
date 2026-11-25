from typing import List

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        vals = {v: i for i, v in enumerate(sorted(set(nums)))}
        rank = [vals[x] for x in nums]
        sa = list(range(n))
        k = 1

        while k < n:
            sa.sort(key=lambda i: (rank[i], rank[i + k] if i + k < n else -1))
            new = [0] * n
            for j in range(1, n):
                a, b = sa[j - 1], sa[j]
                new[b] = new[a] + (
                    (rank[a], rank[a + k] if a + k < n else -1) !=
                    (rank[b], rank[b + k] if b + k < n else -1)
                )
            rank = new
            if rank[sa[-1]] == n - 1:
                break
            k <<= 1

        pos = [0] * n
        for i, x in enumerate(sa):
            pos[x] = i

        lcp = [0] * n
        h = 0
        for i in range(n):
            r = pos[i]
            if r:
                j = sa[r - 1]
                while i + h < n and j + h < n and nums[i + h] == nums[j + h]:
                    h += 1
                lcp[r] = h
                if h:
                    h -= 1

        ans = n
        for r, i in enumerate(sa):
            longest = max(lcp[r], lcp[r + 1] if r + 1 < n else 0)
            length = longest + 1
            if i + length <= n:
                ans = min(ans, length)

        return ans