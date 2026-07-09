class SummaryRanges:

    def __init__(self):
        self.seen = set()

    def addNum(self, value: int) -> None:
        self.seen.add(value)

    def getIntervals(self) -> List[List[int]]:
        intervals = []
        nums = sorted(self.seen)

        i = 0
        while i < len(nums):
            start = nums[i]

            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1

            intervals.append([start, nums[i]])
            i += 1

        return intervals