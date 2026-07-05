class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1] * n
        pointers = [0] * len(primes)
        candidates = primes[:]

        for i in range(1, n):
            next_ugly = min(candidates)
            ugly[i] = next_ugly

            for j in range(len(primes)):
                if candidates[j] == next_ugly:
                    pointers[j] += 1
                    candidates[j] = primes[j] * ugly[pointers[j]]

        return ugly[-1]