from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)

        # bucket[count] stores all numbers occurring exactly `count` times
        bucket = [[] for _ in range(len(nums) + 1)]

        for num, count in frequency.items():
            bucket[count].append(num)

        result = []

        for count in range(len(nums), 0, -1):
            for num in bucket[count]:
                result.append(num)

                if len(result) == k:
                    return result