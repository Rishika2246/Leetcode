class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        from math import gcd
        from functools import reduce

        def lcm(a, b):
            return a // gcd(a, b) * b

        coins = sorted(coins)

        def count(x):
            total = 0
            n = len(coins)

            for mask in range(1, 1 << n):
                cur = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask >> i & 1:
                        cur = lcm(cur, coins[i])
                        bits += 1
                        if cur > x:
                            valid = False
                            break

                if valid:
                    v = x // cur
                    if bits & 1:
                        total += v
                    else:
                        total -= v

            return total

        lo = 1
        hi = min(coins) * k

        while lo < hi:
            mid = (lo + hi) // 2

            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        return lo