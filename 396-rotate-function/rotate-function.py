class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        f = sum(i * x for i, x in enumerate(nums))
        ans = f
        for i in range(n - 1, 0, -1):
            f += s - n * nums[i]
            ans = max(ans, f)
        return ans