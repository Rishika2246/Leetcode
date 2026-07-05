class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        def pick_max(nums, length):
            stack = []
            remove = len(nums) - length

            for digit in nums:
                while stack and remove > 0 and stack[-1] < digit:
                    stack.pop()
                    remove -= 1
                stack.append(digit)

            return stack[:length]

        def merge(a, b):
            result = []

            while a or b:
                if a > b:
                    result.append(a.pop(0))
                else:
                    result.append(b.pop(0))

            return result

        answer = []

        start = max(0, k - len(nums2))
        end = min(k, len(nums1))

        for take1 in range(start, end + 1):
            take2 = k - take1

            part1 = pick_max(nums1, take1)
            part2 = pick_max(nums2, take2)

            candidate = merge(part1, part2)
            answer = max(answer, candidate)

        return answer