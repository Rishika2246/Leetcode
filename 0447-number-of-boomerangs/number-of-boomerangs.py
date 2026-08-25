class Solution:
    def numberOfBoomerangs(self, points: list[list[int]]) -> int:
        ans = 0

        for i in range(len(points)):
            freq = {}

            for j in range(len(points)):
                if i == j:
                    continue

                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                d = dx * dx + dy * dy

                freq[d] = freq.get(d, 0) + 1

            for count in freq.values():
                ans += count * (count - 1)

        return ans