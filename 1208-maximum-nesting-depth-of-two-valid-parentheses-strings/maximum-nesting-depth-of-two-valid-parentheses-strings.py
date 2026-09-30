class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        depth = 0
        ans = []

        for c in seq:
            if c == '(':
                depth += 1
                ans.append(depth & 1)
            else:
                ans.append(depth & 1)
                depth -= 1

        return ans