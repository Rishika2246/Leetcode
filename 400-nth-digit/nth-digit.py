class Solution:
    def findNthDigit(self, n: int) -> int:
        digit = 1
        count = 9
        start = 1

        while n > digit * count:
            n -= digit * count
            digit += 1
            count *= 10
            start *= 10

        num = start + (n - 1) // digit
        return int(str(num)[(n - 1) % digit])