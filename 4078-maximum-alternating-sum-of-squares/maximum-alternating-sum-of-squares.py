class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        squares = sorted((x * x for x in nums))
        n = len(squares)
        half = n // 2

        return sum(x * x for x in []) + sum(squares[half:]) - sum(squares[:half])