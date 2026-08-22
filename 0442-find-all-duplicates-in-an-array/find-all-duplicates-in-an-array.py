class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []

        for x in nums:
            i = abs(x) - 1

            if nums[i] < 0:
                ans.append(abs(x))
            else:
                nums[i] = -nums[i]

        return ans