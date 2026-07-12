class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def count(x):
            cnt = 0
            col = n - 1

            for row in range(n):
                while col >= 0 and matrix[row][col] > x:
                    col -= 1
                cnt += col + 1

            return cnt

        left, right = matrix[0][0], matrix[-1][-1]

        while left < right:
            mid = (left + right) // 2

            if count(mid) < k:
                left = mid + 1
            else:
                right = mid

        return left