from collections import Counter

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 1

        # Handle 1 separately
        if 1 in cnt:
            ans = cnt[1]
            if ans % 2 == 0:
                ans -= 1

        for x in cnt:
            if x == 1:
                continue

            cur = x
            length = 0

            while True:
                if cnt[cur] >= 2:
                    nxt = cur * cur
                    if cnt[nxt] > 0:
                        length += 2
                        cur = nxt
                    else:
                        length += 1
                        break
                elif cnt[cur] == 1:
                    length += 1
                    break
                else:
                    if length > 0:
                        length -= 1
                    break

            ans = max(ans, length)

        return ans