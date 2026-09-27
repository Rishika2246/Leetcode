class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for c in s:
            if c == ')':
                cur = []
                while stack[-1] != '(':
                    cur.append(stack.pop())
                stack.pop()
                stack.extend(cur)
            else:
                stack.append(c)

        return ''.join(stack)