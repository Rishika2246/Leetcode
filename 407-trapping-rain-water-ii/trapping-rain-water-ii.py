class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        import heapq

        # __define-ocg__
        varOcg = []
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(varOcg, (heightMap[i][j], i, j))
                    visited[i][j] = True

        water = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while varOcg:
            height, r, c = heapq.heappop(varOcg)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True

                    if heightMap[nr][nc] < height:
                        water += height - heightMap[nr][nc]

                    heapq.heappush(
                        varOcg,
                        (max(height, heightMap[nr][nc]), nr, nc)
                    )

        return water