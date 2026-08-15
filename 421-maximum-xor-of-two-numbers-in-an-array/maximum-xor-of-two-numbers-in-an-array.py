class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        mask = 0

        for i in range(30, -1, -1):
            mask |= 1 << i
            prefixes = {num & mask for num in nums}

            candidate = ans | (1 << i)

            for p in prefixes:
                if p ^ candidate in prefixes:
                    ans = candidate
                    break

        return ans