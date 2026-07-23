class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def dfs(t):
            if len(t) < k:
                return 0
            cnt = {}
            for c in t:
                cnt[c] = cnt.get(c, 0) + 1
            for c, v in cnt.items():
                if v < k:
                    return max(dfs(x) for x in t.split(c))
            return len(t)

        return dfs(s)