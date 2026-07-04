class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        n = len(nums)

        # Minimum value available on the right side
        suffix_min = nums[-1]
        answer = float("-inf")

        # Build prefix sum while moving the split from right to left
        prefix_sum = sum(nums[:-1])

        for i in range(n - 2, -1, -1):
            answer = max(answer, prefix_sum - suffix_min)

            suffix_min = min(suffix_min, nums[i])
            prefix_sum -= nums[i]

        return answer