class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Same starting point → longer interval must come first
        intervals.sort(key=lambda x: (x[0], -x[1]))

        remaining = 0
        farthest_end = 0

        for start, end in intervals:
            if end > farthest_end:
                remaining += 1
                farthest_end = end

        return remaining