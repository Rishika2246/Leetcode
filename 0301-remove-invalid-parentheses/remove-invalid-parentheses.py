class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left_remove = right_remove = 0

        for ch in s:
            if ch == '(':
                left_remove += 1
            elif ch == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        result = set()

        def backtrack(index, left_count, right_count, left_rem, right_rem, path):
            if index == len(s):
                if left_count == right_count:
                    result.add("".join(path))
                return

            ch = s[index]

            if ch == '(' and left_rem > 0:
                backtrack(index + 1, left_count, right_count,
                          left_rem - 1, right_rem, path)

            if ch == ')' and right_rem > 0:
                backtrack(index + 1, left_count, right_count,
                          left_rem, right_rem - 1, path)

            path.append(ch)

            if ch not in '()':
                backtrack(index + 1, left_count, right_count,
                          left_rem, right_rem, path)

            elif ch == '(':
                backtrack(index + 1, left_count + 1, right_count,
                          left_rem, right_rem, path)

            elif right_count < left_count:
                backtrack(index + 1, left_count, right_count + 1,
                          left_rem, right_rem, path)

            path.pop()

        backtrack(0, 0, 0, left_remove, right_remove, [])
        return list(result)