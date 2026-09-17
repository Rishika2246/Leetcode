class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        INF = n + 1
        best = [INF] * n

        left = 0
        curr = 0
        ans = INF

        for right in range(n):
            curr += arr[right]

            while curr > target:
                curr -= arr[left]
                left += 1

            if right > 0:
                best[right] = best[right - 1]

            if curr == target:
                length = right - left + 1

                if left > 0 and best[left - 1] < INF:
                    ans = min(ans, length + best[left - 1])

                best[right] = min(best[right], length)

        return ans if ans < INF else -1
        