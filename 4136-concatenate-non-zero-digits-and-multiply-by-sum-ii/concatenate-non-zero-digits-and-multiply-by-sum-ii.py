class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        # prefix_sum[i] = sum of non-zero digits in s[0:i]
        prefix_sum = [0] * (n + 1)

        # value[i] = number formed by non-zero digits in s[0:i]
        value = [0] * (n + 1)

        # power[k] = 10^k mod MOD
        power = [1] * (n + 1)

        # count[i] = number of non-zero digits in s[0:i]
        count = [0] * (n + 1)

        for i, ch in enumerate(s):
            digit = int(ch)

            prefix_sum[i + 1] = prefix_sum[i]
            value[i + 1] = value[i]
            count[i + 1] = count[i]
            power[i + 1] = (power[i] * 10) % MOD

            if digit != 0:
                prefix_sum[i + 1] += digit
                count[i + 1] += 1
                value[i + 1] = (value[i] * 10 + digit) % MOD

        answer = []

        for left, right in queries:
            digit_sum = prefix_sum[right + 1] - prefix_sum[left]

            non_zero_digits = count[right + 1] - count[left]

            x = (
                value[right + 1]
                - value[left] * power[non_zero_digits]
            ) % MOD

            answer.append((x * digit_sum) % MOD)

        return answer