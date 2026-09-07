class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = 1
        last = [0] * 26

        for c in s:
            x = ord(c) - 97
            new = (dp * 2 - last[x]) % MOD
            last[x] = dp
            dp = new

        return (dp - 1) % MOD