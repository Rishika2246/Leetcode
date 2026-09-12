from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        n = len(intervals)
        arr = sorted((l, r, w, i) for i, (l, r, w) in enumerate(intervals))
        starts = [x[0] for x in arr]

        nxt = [bisect_right(starts, arr[i][1]) for i in range(n)]

        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            l, r, w, idx = arr[i]

            for k in range(1, 5):
                skip_score, skip_ids = dp[i + 1][k]

                take_score, take_ids = dp[nxt[i]][k - 1]
                take_score += w
                take_ids = tuple(sorted(take_ids + (idx,)))

                if take_score > skip_score or (
                    take_score == skip_score and take_ids < skip_ids
                ):
                    dp[i][k] = (take_score, take_ids)
                else:
                    dp[i][k] = (skip_score, skip_ids)

        return list(dp[0][4][1])