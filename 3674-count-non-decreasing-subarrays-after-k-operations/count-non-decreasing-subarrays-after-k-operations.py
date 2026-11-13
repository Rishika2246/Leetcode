from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nxt = [-1] * n
        stack = []

        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                nxt[stack.pop()] = i
            stack.append(i)

        LOG = n.bit_length()
        up = [nxt]
        sums = [[nums[i] * ((nxt[i] if nxt[i] != -1 else n) - i) for i in range(n)]]

        for j in range(1, LOG):
            prev = up[-1]
            ps = sums[-1]
            cur = [-1] * n
            sm = [0] * n

            for i, mid in enumerate(prev):
                if mid != -1:
                    cur[i] = prev[mid]
                    sm[i] = ps[i] + ps[mid]

            up.append(cur)
            sums.append(sm)

        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        def get_cost(l, r):
            cur = l
            total = 0

            for j in range(LOG - 1, -1, -1):
                v = up[j][cur]
                if v != -1 and v <= r:
                    total += sums[j][cur]
                    cur = v

            total += nums[cur] * (r - cur + 1)
            return total - (pref[r + 1] - pref[l])

        ans = left = 0

        for right in range(n):
            while get_cost(left, right) > k:
                left += 1
            ans += right - left + 1

        return ans