class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = [0]
        ans = 0

        for line in input.split('\n'):
            level = line.count('\t')
            name = line.lstrip('\t')

            while len(stack) > level + 1:
                stack.pop()

            curr = stack[-1] + len(name)

            if '.' in name:
                ans = max(ans, curr)
            else:
                stack.append(curr + 1)

        return ans