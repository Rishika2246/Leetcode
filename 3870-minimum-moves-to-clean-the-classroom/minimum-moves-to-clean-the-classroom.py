from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m, n = len(classroom), len(classroom[0])

        start = None
        litter = []
        for r in range(m):
            for c in range(n):
                ch = classroom[r][c]
                if ch == 'S':
                    start = (r, c)
                elif ch == 'L':
                    litter.append((r, c))

        k = len(litter)
        if k == 0:
            return 0

        lid = {p: i for i, p in enumerate(litter)}
        target = (1 << k) - 1

        # BFS state: (position, collected_mask, energy)
        # For the same (position, mask), only the maximum remaining
        # energy needs to be kept.
        best = [[[-1] * (1 << k) for _ in range(n)] for _ in range(m)]

        sr, sc = start
        best[sr][sc][0] = energy

        q = deque([(sr, sc, 0, energy)])
        dist = 0
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while q:
            for _ in range(len(q)):
                r, c, mask, e = q.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if not (0 <= nr < m and 0 <= nc < n):
                        continue
                    if classroom[nr][nc] == 'X':
                        continue

                    ne = e - 1
                    if ne < 0:
                        continue

                    nmask = mask

                    if classroom[nr][nc] == 'L':
                        nmask |= 1 << lid[(nr, nc)]

                    if classroom[nr][nc] == 'R':
                        ne = energy

                    if nmask == target:
                        return dist + 1

                    # Dominance pruning:
                    # If we've reached the same position/mask with
                    # >= remaining energy, this state is useless.
                    if ne <= best[nr][nc][nmask]:
                        continue

                    best[nr][nc][nmask] = ne
                    q.append((nr, nc, nmask, ne))

            dist += 1

        return -1