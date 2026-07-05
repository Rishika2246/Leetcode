class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        pairs = [(nums[i], i) for i in range(n)]

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            merged = []
            i = j = 0
            smaller_count = 0

            while i < len(left) and j < len(right):
                if left[i][0] <= right[j][0]:
                    result[left[i][1]] += smaller_count
                    merged.append(left[i])
                    i += 1
                else:
                    smaller_count += 1
                    merged.append(right[j])
                    j += 1

            while i < len(left):
                result[left[i][1]] += smaller_count
                merged.append(left[i])
                i += 1

            merged.extend(right[j:])
            return merged

        merge_sort(pairs)
        return result