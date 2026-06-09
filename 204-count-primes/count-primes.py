class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        prime = [True] * n
        prime[0] = prime[1] = False

        p = 2
        while p * p < n:
            if prime[p]:
                for multiple in range(p * p, n, p):
                    prime[multiple] = False
            p += 1

        return sum(prime)