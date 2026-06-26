from functools import lru_cache

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        @lru_cache(None)
        def solve(exp):
            res = []

            for i, ch in enumerate(exp):
                if ch in "+-*":
                    left = solve(exp[:i])
                    right = solve(exp[i + 1:])

                    for a in left:
                        for b in right:
                            if ch == '+':
                                res.append(a + b)
                            elif ch == '-':
                                res.append(a - b)
                            else:
                                res.append(a * b)

            if not res:
                res.append(int(exp))

            return res

        return solve(expression)