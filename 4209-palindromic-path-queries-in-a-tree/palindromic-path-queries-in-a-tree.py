from typing import List

class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        chars = [ord(c) - 97 for c in s]
        par = [0] * n
        depth = [0] * n
        base = [0] * n          # XOR mask from root to node (initial string)
        tin = [0] * n
        size = [1] * n
        order = []

        # iterative preorder DFS
        stack = [0]
        par[0] = 0
        visited = [False] * n
        visited[0] = True
        base[0] = 1 << chars[0]
        while stack:
            u = stack.pop()
            tin[u] = len(order)
            order.append(u)
            for w in adj[u]:
                if not visited[w]:
                    visited[w] = True
                    par[w] = u
                    depth[w] = depth[u] + 1
                    base[w] = base[u] ^ (1 << chars[w])
                    stack.append(w)
        for u in reversed(order):
            if u != 0:
                size[par[u]] += size[u]

        # binary lifting for LCA
        LOG = max(1, (n).bit_length())
        up = [par]
        for j in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[v]] for v in range(n)])

        def lca(a: int, b: int) -> int:
            if depth[a] < depth[b]:
                a, b = b, a
            diff = depth[a] - depth[b]
            j = 0
            while diff:
                if diff & 1:
                    a = up[j][a]
                diff >>= 1
                j += 1
            if a == b:
                return a
            for j in range(LOG - 1, -1, -1):
                if up[j][a] != up[j][b]:
                    a = up[j][a]
                    b = up[j][b]
            return par[a]

        # XOR Fenwick tree: range XOR update, point query
        tree = [0] * (n + 2)

        def add(i: int, val: int) -> None:
            i += 1
            while i <= n + 1:
                tree[i] ^= val
                i += i & -i

        def point(i: int) -> int:
            i += 1
            r = 0
            while i > 0:
                r ^= tree[i]
                i -= i & -i
            return r

        def cur(x: int) -> int:
            return base[x] ^ point(tin[x])

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = ord(parts[2]) - 97
                if chars[u] != c:
                    d = (1 << chars[u]) ^ (1 << c)
                    chars[u] = c
                    add(tin[u], d)
                    add(tin[u] + size[u], d)
            else:
                u, v = int(parts[1]), int(parts[2])
                l = lca(u, v)
                mask = cur(u) ^ cur(v) ^ (1 << chars[l])
                ans.append(mask & (mask - 1) == 0)
        return ans