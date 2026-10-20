from typing import List

class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for k in range(1, n + 1):
            if n % k:
                continue
            ok = True
            prev_max = 0
            for s in range(0, n, k):
                e = s + k - 1
                d = 0
                j = -1
                for i in range(s, e):
                    if nums[i] > nums[i + 1]:
                        d += 1
                        j = i
                        if d > 1:
                            break
                if d > 1:
                    ok = False
                    break
                if d == 0:
                    lo, hi = nums[s], nums[e]
                else:
                    # rotation of a sorted block requires wrap-around to be non-descending
                    if nums[e] > nums[s]:
                        ok = False
                        break
                    lo, hi = nums[j + 1], nums[j]
                if lo < prev_max:
                    ok = False
                    break
                prev_max = hi
            if ok:
                total += k
        return total