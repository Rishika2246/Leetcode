class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        left = num[:half]
        right = num[half:]

        left_sum = sum(int(c) for c in left if c != '?')
        right_sum = sum(int(c) for c in right if c != '?')

        left_q = left.count('?')
        right_q = right.count('?')

        # Odd number of '?' means Alice can always force inequality
        if (left_q + right_q) % 2:
            return True

        # Bob can win only if the difference can be exactly balanced
        return left_sum - right_sum != 9 * (right_q - left_q) // 2