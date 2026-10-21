class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        mn, mx = min(s), max(s)

        # Already sorted
        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0

        # Length 2 and unsorted: only possible substrings have length 1
        if n == 2:
            return -1

        # One operation: sort s[1:] (needs s[0] to be the minimum)
        # or sort s[:-1] (needs s[-1] to be the maximum)
        if s[0] == mn or s[-1] == mx:
            return 1

        # Three operations only if the unique max is at the front
        # and the unique min is at the end
        if s[0] == mx and s.count(mx) == 1 and s[-1] == mn and s.count(mn) == 1:
            return 3

        return 2