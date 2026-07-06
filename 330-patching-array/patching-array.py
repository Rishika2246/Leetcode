class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        i = 0
        covered = 0  # Can currently form every sum from 1 to covered

        while covered < n:
            if i < len(nums) and nums[i] <= covered + 1:
                covered += nums[i]
                i += 1
            else:
                # covered + 1 is the smallest missing sum, so patch it
                covered += covered + 1
                patches += 1

        return patches