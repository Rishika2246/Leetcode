class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for x in nums:
            i = abs(x) - 1
            nums[i] = -abs(nums[i])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]