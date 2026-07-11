class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX = 0x7FFFFFFF

        while b:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

        return a if a <= MAX else ~(a ^ MASK)