class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = [0, 0, 0]

        for x in stones:
            cnt[x % 3] += 1

        zero, one, two = cnt

        if one == 0 and two == 0:
            return False

        if zero % 2 == 0:
            return one > 0 and two > 0

        return abs(one - two) > 2