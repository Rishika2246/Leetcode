class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        odd = even = 0
        prefix = 0
        ans = 0

        for num in arr:
            prefix += num

            if prefix % 2:
                ans += even + 1
                odd += 1
            else:
                ans += odd
                even += 1

        return ans % MOD