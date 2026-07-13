class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        num = ""
        negative = False

        for c in s:
            if c == '[':
                stack.append(NestedInteger())
            elif c == '-':
                negative = True
            elif c.isdigit():
                num += c
            else:
                if num:
                    val = int(num)
                    if negative:
                        val = -val
                    stack[-1].add(NestedInteger(val))
                    num = ""
                    negative = False
                if c == ']' and len(stack) > 1:
                    ni = stack.pop()
                    stack[-1].add(ni)

        return stack[0]