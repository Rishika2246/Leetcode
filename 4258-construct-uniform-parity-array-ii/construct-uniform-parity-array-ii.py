class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mn_odd = min((x for x in nums1 if x % 2), default=float('inf'))
        mn_even = min((x for x in nums1 if x % 2 == 0), default=float('inf'))

        return mn_odd == float('inf') or mn_odd < mn_even