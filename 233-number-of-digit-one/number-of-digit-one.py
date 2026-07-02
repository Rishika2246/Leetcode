class Solution:
    def countDigitOne(self, n: int) -> int:
        ans = 0
        place = 1

        while place <= n:
            higher = n // (place * 10)
            cur = (n // place) % 10
            lower = n % place

            if cur == 0:
                ans += higher * place
            elif cur == 1:
                ans += higher * place + lower + 1
            else:
                ans += (higher + 1) * place

            place *= 10

        return ans