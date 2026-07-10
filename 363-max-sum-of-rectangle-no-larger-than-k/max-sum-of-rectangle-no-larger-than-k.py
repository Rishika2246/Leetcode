from bisect import bisect_left, insort

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        rows, cols = len(matrix), len(matrix[0])

        if rows > cols:
            matrix = list(zip(*matrix))
            rows, cols = cols, rows

        ans = float("-inf")

        for top in range(rows):
            col_sums = [0] * cols

            for bottom in range(top, rows):
                for c in range(cols):
                    col_sums[c] += matrix[bottom][c]

                prefix = 0
                sorted_prefix = [0]
                best = float("-inf")

                for value in col_sums:
                    prefix += value
                    idx = bisect_left(sorted_prefix, prefix - k)

                    if idx < len(sorted_prefix):
                        best = max(best, prefix - sorted_prefix[idx])

                    insort(sorted_prefix, prefix)

                ans = max(ans, best)

                if ans == k:
                    return k

        return ans