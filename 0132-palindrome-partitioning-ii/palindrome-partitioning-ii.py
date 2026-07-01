class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        # dp[i] = min cuts for s[:i]
        dp = [0] * (n + 1)
        for i in range(n + 1):
            dp[i] = i - 1
        
        # palindrome table
        is_pal = [[False]*n for _ in range(n)]
        
        for end in range(n):
            for start in range(end + 1):
                if s[start] == s[end] and (end - start <= 2 or is_pal[start + 1][end - 1]):
                    is_pal[start][end] = True
                    dp[end + 1] = min(dp[end + 1], dp[start] + 1)
        
        return dp[n]