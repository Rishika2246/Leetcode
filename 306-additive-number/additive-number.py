class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        for i in range(1, n):
            # First number cannot have leading zero
            if num[0] == '0' and i > 1:
                break

            for j in range(i + 1, n):
                # Second number cannot have leading zero
                if num[i] == '0' and j - i > 1:
                    break

                first = int(num[:i])
                second = int(num[i:j])
                pos = j

                while pos < n:
                    third = first + second
                    third_str = str(third)

                    if not num.startswith(third_str, pos):
                        break

                    pos += len(third_str)
                    first, second = second, third

                if pos == n:
                    return True

        return False