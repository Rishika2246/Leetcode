class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_all = 0

        # XOR of the two unique numbers
        for num in nums:
            xor_all ^= num

        # Rightmost bit where the two unique numbers differ
        diff_bit = xor_all & -xor_all

        first = 0
        second = 0

        # Separate numbers into two groups using that differing bit
        for num in nums:
            if num & diff_bit:
                first ^= num
            else:
                second ^= num

        return [first, second]