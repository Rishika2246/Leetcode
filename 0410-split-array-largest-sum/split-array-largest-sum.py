class Solution:
    def splitArray(self, nums, k):
        left = max(nums)
        right = sum(nums)

        def canSplit(maxSum):
            parts = 1
            curr = 0

            for num in nums:
                if curr + num > maxSum:
                    parts += 1
                    curr = num
                else:
                    curr += num

            return parts <= k

        while left < right:
            mid = (left + right) // 2

            if canSplit(mid):
                right = mid
            else:
                left = mid + 1

        return left