class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(string):
            balance = 0

            for ch in string:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        left = right = 0

        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1

        result = set()

        def backtrack(i, path, left_rem, right_rem, balance):
            if i == len(s):
                if left_rem == 0 and right_rem == 0 and balance == 0:
                    result.add(''.join(path))
                return

            ch = s[i]

            if ch == '(':
                if left_rem > 0:
                    backtrack(i + 1, path, left_rem - 1, right_rem, balance)

                path.append(ch)
                backtrack(i + 1, path, left_rem, right_rem, balance + 1)
                path.pop()

            elif ch == ')':
                if right_rem > 0:
                    backtrack(i + 1, path, left_rem, right_rem - 1, balance)

                if balance > 0:
                    path.append(ch)
                    backtrack(i + 1, path, left_rem, right_rem, balance - 1)
                    path.pop()

            else:
                path.append(ch)
                backtrack(i + 1, path, left_rem, right_rem, balance)
                path.pop()

        backtrack(0, [], left, right, 0)
        return list(result)