class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        n = len(nums)

        # Put smaller half at even indexes, larger half at odd indexes
        small = nums[:(n + 1) // 2][::-1]
        large = nums[(n + 1) // 2:][::-1]

        nums[::2] = small
        nums[1::2] = large