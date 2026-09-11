class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        cnt = [0] * 10
        for d in digits:
            cnt[d] += 1

        ans = 0

        for a in range(1, 10):
            if cnt[a] == 0:
                continue
            cnt[a] -= 1

            for b in range(10):
                if cnt[b] == 0:
                    continue
                cnt[b] -= 1

                for c in range(0, 10, 2):
                    if cnt[c]:
                        ans += 1

                cnt[b] += 1

            cnt[a] += 1

        return ans