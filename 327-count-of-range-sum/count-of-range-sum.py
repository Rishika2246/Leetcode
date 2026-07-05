class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        def merge_sort(left: int, right: int) -> int:
            if right - left <= 1:
                return 0

            mid = (left + right) // 2
            count = merge_sort(left, mid) + merge_sort(mid, right)

            low = high = mid

            for i in range(left, mid):
                while low < right and prefix[low] - prefix[i] < lower:
                    low += 1

                while high < right and prefix[high] - prefix[i] <= upper:
                    high += 1

                count += high - low

            prefix[left:right] = sorted(prefix[left:right])
            return count

        return merge_sort(0, len(prefix))