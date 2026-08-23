class Solution:
    def maxBuilding(self, n: int, restrictions: list[list[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.sort()

        # Forward pass
        for i in range(1, len(restrictions)):
            prev_id, prev_h = restrictions[i - 1]
            curr_id, curr_h = restrictions[i]
            restrictions[i][1] = min(curr_h, prev_h + curr_id - prev_id)

        # Backward pass
        for i in range(len(restrictions) - 2, -1, -1):
            curr_id, curr_h = restrictions[i]
            next_id, next_h = restrictions[i + 1]
            restrictions[i][1] = min(curr_h, next_h + next_id - curr_id)

        ans = 0

        for i in range(len(restrictions) - 1):
            id1, h1 = restrictions[i]
            id2, h2 = restrictions[i + 1]

            dist = id2 - id1

            # Maximum peak between two restricted buildings
            ans = max(ans, (h1 + h2 + dist) // 2)

        # Buildings after the last restriction can keep increasing by 1
        last_id, last_h = restrictions[-1]
        ans = max(ans, last_h + (n - last_id))

        return ans