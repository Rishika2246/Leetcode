class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        def bfs(starts):
            seen = set(starts)
            q = deque(starts)

            while q:
                r, c = q.popleft()

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < m and 0 <= nc < n and
                        (nr, nc) not in seen and
                        heights[nr][nc] >= heights[r][c]):
                        seen.add((nr, nc))
                        q.append((nr, nc))

            return seen

        pacific = [(0, c) for c in range(n)] + [(r, 0) for r in range(m)]
        atlantic = [(m - 1, c) for c in range(n)] + [(r, n - 1) for r in range(m)]

        p = bfs(pacific)
        a = bfs(atlantic)

        return [[r, c] for r, c in p & a]