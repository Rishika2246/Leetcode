class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        freq = [0] * (max(costs) + 1)

        for cost in costs:
            freq[cost] += 1

        ans = 0

        for cost in range(1, len(freq)):
            if freq[cost] == 0:
                continue

            can_buy = min(freq[cost], coins // cost)
            ans += can_buy
            coins -= can_buy * cost

            if coins < cost:
                break

        return ans