class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        s = list(s)

        # Tree stores: left run, right run, best run, length
        tree = [[0, 0, 0, 0] for _ in range(4 * n)]

        def build(node, l, r):
            if l == r:
                tree[node] = [1, 1, 1, 1]
                return

            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)
            pull(node, l, r)

        def pull(node, l, r):
            left = node * 2
            right = left + 1
            mid = (l + r) // 2

            ll, lr, lb, llen = tree[left]
            rl, rr, rb, rlen = tree[right]

            left_run = ll
            if ll == llen and s[mid] == s[mid + 1]:
                left_run = llen + rl

            right_run = rr
            if rr == rlen and s[mid] == s[mid + 1]:
                right_run = rlen + lr

            best = max(lb, rb)
            if s[mid] == s[mid + 1]:
                best = max(best, lr + rl)

            tree[node] = [left_run, right_run, best, llen + rlen]

        def update(node, l, r, idx):
            if l == r:
                tree[node] = [1, 1, 1, 1]
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx)
            else:
                update(node * 2 + 1, mid + 1, r, idx)

            pull(node, l, r)

        build(1, 0, n - 1)

        ans = []

        for ch, idx in zip(queryCharacters, queryIndices):
            s[idx] = ch
            update(1, 0, n - 1, idx)
            ans.append(tree[1][2])

        return ans