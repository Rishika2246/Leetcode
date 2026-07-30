class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for d in num:
            while k and stack and stack[-1] > d:
                stack.pop()
                k -= 1
            stack.append(d)

        while k:
            stack.pop()
            k -= 1

        ans = ''.join(stack).lstrip('0')
        return ans if ans else "0"