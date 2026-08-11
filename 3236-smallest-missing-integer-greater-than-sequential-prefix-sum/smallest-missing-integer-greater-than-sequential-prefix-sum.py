class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        total = nums[0]

        # Find sequential prefix sum
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        # Find smallest integer >= total that is not in nums
        nums_set = set(nums)

        while total in nums_set:
            total += 1

        return total