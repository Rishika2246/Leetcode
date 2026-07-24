from collections import defaultdict
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.mp = defaultdict(list)
        for i, x in enumerate(nums):
            self.mp[x].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.mp[target])

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)