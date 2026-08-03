class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        if num < 0:
            num += 1 << 32

        digits = "0123456789abcdef"
        ans = []

        while num:
            ans.append(digits[num & 15])
            num >>= 4

        return "".join(reversed(ans))