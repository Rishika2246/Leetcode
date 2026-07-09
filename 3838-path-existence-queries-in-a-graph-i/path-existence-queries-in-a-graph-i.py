class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[bool]:

        # component[i] = connected component number of node i
        component = [0] * n
        group = 0

        for i in range(1, n):
            # A gap larger than maxDiff breaks connectivity.
            if nums[i] - nums[i - 1] > maxDiff:
                group += 1

            component[i] = group

        return [component[u] == component[v] for u, v in queries]