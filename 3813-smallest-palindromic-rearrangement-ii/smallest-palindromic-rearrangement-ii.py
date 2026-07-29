from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = Counter(s)

        half = [0] * 26
        mid = ""
        m = 0

        for i in range(26):
            c = chr(ord('a') + i)
            half[i] = cnt[c] // 2
            m += half[i]
            if cnt[c] & 1:
                mid = c

        LIMIT = 10 ** 6 + 1

        def count_perm(freq):
            rem = sum(freq)
            res = 1
            for x in freq:
                if x:
                    res *= comb(rem, x)
                    if res > LIMIT:
                        return LIMIT
                    rem -= x
            return res

        if count_perm(half) < k:
            return ""

        left = []

        for _ in range(m):
            for i in range(26):
                if half[i] == 0:
                    continue

                half[i] -= 1
                ways = count_perm(half)

                if ways >= k:
                    left.append(chr(i + ord('a')))
                    break

                k -= ways
                half[i] += 1

        left = "".join(left)
        return left + mid + left[::-1]