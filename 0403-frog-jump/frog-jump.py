class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_set = set(stones)
        last = stones[-1]

        dp = {stone: set() for stone in stones}
        dp[0].add(0)

        for stone in stones:
            for k in dp[stone]:
                for jump in (k - 1, k, k + 1):
                    if jump > 0:
                        nxt = stone + jump
                        if nxt == last:
                            return True
                        if nxt in stone_set:
                            dp[nxt].add(jump)

        return last == 0