class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)

        arr = sorted((x, i) for i, x in enumerate(nums))

        ans = [0] * n
        l = 0

        while l < n:
            r = l

            # Values belong to the same swappable component
            # if consecutive sorted values differ by <= limit.
            while r + 1 < n and arr[r + 1][0] - arr[r][0] <= limit:
                r += 1

            values = [arr[i][0] for i in range(l, r + 1)]
            indices = sorted(arr[i][1] for i in range(l, r + 1))

            for idx, val in zip(indices, values):
                ans[idx] = val

            l = r + 1

        return ans