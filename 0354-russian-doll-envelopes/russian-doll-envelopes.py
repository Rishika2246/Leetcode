from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Same widths: taller envelope first, so equal-width envelopes
        # cannot be incorrectly included in the LIS.
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        tails = []

        for _, height in envelopes:
            pos = bisect_left(tails, height)

            if pos == len(tails):
                tails.append(height)
            else:
                tails[pos] = height

        return len(tails)