class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 3:
            return 1

        s = [1, 2, 2]
        head = 2
        num = 1
        ones = 1

        while len(s) < n:
            count = s[head]

            for _ in range(count):
                s.append(num)
                if num == 1 and len(s) <= n:
                    ones += 1

            num = 3 - num
            head += 1

        return ones