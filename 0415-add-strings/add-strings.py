class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        res = []

        while i >= 0 or j >= 0 or carry:
            a = ord(num1[i]) - ord('0') if i >= 0 else 0
            b = ord(num2[j]) - ord('0') if j >= 0 else 0

            total = a + b + carry
            res.append(str(total % 10))
            carry = total // 10

            i -= 1
            j -= 1

        return ''.join(reversed(res))