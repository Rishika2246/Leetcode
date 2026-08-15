class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)

        missing = 3
        if any(c.islower() for c in password):
            missing -= 1
        if any(c.isupper() for c in password):
            missing -= 1
        if any(c.isdigit() for c in password):
            missing -= 1

        runs = []
        i = 0
        while i < n:
            j = i
            while j < n and password[j] == password[i]:
                j += 1
            if j - i >= 3:
                runs.append(j - i)
            i = j

        replace = sum(x // 3 for x in runs)

        if n < 6:
            return max(6 - n, missing)

        if n <= 20:
            return max(replace, missing)

        delete = n - 20
        remain = delete

        # Delete from runs where x % 3 == 0 first
        for r in runs:
            if remain > 0 and r % 3 == 0:
                d = min(remain, 1)
                replace -= d
                remain -= d

        # Then runs where x % 3 == 1
        for r in runs:
            if remain > 0 and r % 3 == 1:
                d = min(remain, 2)
                replace -= d // 2
                remain -= d

        # Finally, delete 3 characters to reduce one replacement
        replace -= remain // 3

        return delete + max(replace, missing)