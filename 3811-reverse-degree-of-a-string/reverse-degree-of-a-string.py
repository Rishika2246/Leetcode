class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((27 - (ord(c) - ord('a') + 1)) * i
                   for i, c in enumerate(s, 1))