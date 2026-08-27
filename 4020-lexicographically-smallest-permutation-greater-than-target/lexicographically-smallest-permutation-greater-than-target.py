class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - 97] += 1

        n = len(target)

        # Find the rightmost position where we can make
        # the permutation strictly greater than target.
        possible = -1
        work = cnt[:]

        for i in range(n):
            x = ord(target[i]) - 97

            # At this position, can we choose something > target[i]?
            for c in range(x + 1, 26):
                if work[c]:
                    possible = i
                    break

            # Continue matching target if possible.
            if work[x] == 0:
                break

            work[x] -= 1

        if possible == -1:
            return ""

        # Rebuild using target's prefix up to 'possible'.
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        ans = []

        for i in range(possible):
            x = ord(target[i]) - 97
            ans.append(target[i])
            cnt[x] -= 1

        x = ord(target[possible]) - 97

        # Smallest available character strictly greater than target[possible].
        for c in range(x + 1, 26):
            if cnt[c]:
                ans.append(chr(c + 97))
                cnt[c] -= 1
                break

        # Fill suffix with smallest possible characters.
        for c in range(26):
            if cnt[c]:
                ans.extend([chr(c + 97)] * cnt[c])

        return ''.join(ans)