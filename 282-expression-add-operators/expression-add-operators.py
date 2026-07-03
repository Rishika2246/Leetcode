class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []

        def backtrack(index, expression, total, previous):
            if index == len(num):
                if total == target:
                    ans.append(expression)
                return

            for end in range(index + 1, len(num) + 1):
                # Prevent numbers like "05", "00", etc.
                if end > index + 1 and num[index] == '0':
                    break

                part = num[index:end]
                value = int(part)

                if index == 0:
                    backtrack(end, part, value, value)
                else:
                    backtrack(end, expression + "+" + part,
                              total + value, value)

                    backtrack(end, expression + "-" + part,
                              total - value, -value)

                    # Undo previous value, then add multiplied value
                    backtrack(end, expression + "*" + part,
                              total - previous + previous * value,
                              previous * value)

        backtrack(0, "", 0, 0)
        return ans