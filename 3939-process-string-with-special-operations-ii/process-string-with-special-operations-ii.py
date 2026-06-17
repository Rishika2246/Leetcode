class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)

        lengths = [0] * (n + 1)
        for i, ch in enumerate(s):
            cur = lengths[i]

            if 'a' <= ch <= 'z':
                lengths[i + 1] = cur + 1
            elif ch == '*':
                lengths[i + 1] = max(0, cur - 1)
            elif ch == '#':
                lengths[i + 1] = cur * 2
            else:  # '%'
                lengths[i + 1] = cur

        if k >= lengths[n]:
            return '.'

        for i in range(n - 1, -1, -1):
            ch = s[i]
            prev = lengths[i]
            curr = lengths[i + 1]

            if 'a' <= ch <= 'z':
                if k == prev:
                    return ch

            elif ch == '*':
                pass

            elif ch == '#':
                if k >= prev:
                    k -= prev

            else:  # '%'
                k = curr - 1 - k

        return '.'