class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}

        for r, s in reservedSeats:
            rows[r] = rows.get(r, 0) | (1 << s)

        ans = (n - len(rows)) * 2

        left_mask = (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5)
        mid_mask = (1 << 4) | (1 << 5) | (1 << 6) | (1 << 7)
        right_mask = (1 << 6) | (1 << 7) | (1 << 8) | (1 << 9)

        for mask in rows.values():
            left = (mask & left_mask) == 0
            mid = (mask & mid_mask) == 0
            right = (mask & right_mask) == 0

            if left and right:
                ans += 2
            elif left or mid or right:
                ans += 1

        return ans