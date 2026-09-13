class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)
        a = [(i, j) for i in range(n) for j in range(n) if img1[i][j]]
        b = [(i, j) for i in range(n) for j in range(n) if img2[i][j]]

        shifts = {}
        ans = 0

        for x1, y1 in a:
            for x2, y2 in b:
                shift = (x2 - x1, y2 - y1)
                shifts[shift] = shifts.get(shift, 0) + 1
                ans = max(ans, shifts[shift])

        return ans