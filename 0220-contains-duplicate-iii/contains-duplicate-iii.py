class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:

        if valueDiff < 0:
            return False

        buckets = {}
        w = valueDiff + 1

        for i, num in enumerate(nums):

            bucket = num // w

            if bucket in buckets:
                return True

            if bucket - 1 in buckets and abs(num - buckets[bucket - 1]) <= valueDiff:
                return True

            if bucket + 1 in buckets and abs(num - buckets[bucket + 1]) <= valueDiff:
                return True

            buckets[bucket] = num

            if i >= indexDiff:
                old = nums[i - indexDiff]
                del buckets[old // w]

        return False