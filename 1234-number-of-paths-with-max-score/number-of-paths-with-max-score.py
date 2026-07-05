class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)

        # dp[r][c] = [maximum score to reach this cell, number of ways]
        dp = [[[-1, 0] for _ in range(n)] for _ in range(n)]
        dp[n - 1][n - 1] = [0, 1]   # Start at S

        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if board[r][c] == "X" or (r == n - 1 and c == n - 1):
                    continue

                best_score = -1
                ways = 0

                # Previous reachable cells: below, right, diagonal below-right
                for nr, nc in ((r + 1, c), (r, c + 1), (r + 1, c + 1)):
                    if nr < n and nc < n:
                        prev_score, prev_ways = dp[nr][nc]

                        if prev_score > best_score:
                            best_score = prev_score
                            ways = prev_ways
                        elif prev_score == best_score and prev_score != -1:
                            ways = (ways + prev_ways) % MOD

                if best_score != -1:
                    value = 0 if board[r][c] == "E" else int(board[r][c])
                    dp[r][c] = [best_score + value, ways]

        score, ways = dp[0][0]
        return [score, ways] if score != -1 else [0, 0]