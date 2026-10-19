class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        smaller = sum(x < target for x in nums)
        equal = nums.count(target)
        return list(range(smaller, smaller + equal))