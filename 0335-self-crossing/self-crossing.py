class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        for i in range(3, len(distance)):
            # Case 1: current line crosses the line 3 steps before it
            if distance[i] >= distance[i - 2] and distance[i - 1] <= distance[i - 3]:
                return True

            # Case 2: current line touches the line 4 steps before it
            if (
                i >= 4
                and distance[i - 1] == distance[i - 3]
                and distance[i] + distance[i - 4] >= distance[i - 2]
            ):
                return True

            # Case 3: current line crosses the line 5 steps before it
            if (
                i >= 5
                and distance[i - 2] >= distance[i - 4]
                and distance[i] >= distance[i - 2] - distance[i - 4]
                and distance[i - 1] >= distance[i - 3] - distance[i - 5]
                and distance[i - 1] <= distance[i - 3]
            ):
                return True

        return False