class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]   # holding one stock
        sold = 0            # just sold today
        rest = 0            # not holding, can buy

        for price in prices[1:]:
            prev_hold = hold
            prev_sold = sold
            prev_rest = rest

            hold = max(prev_hold, prev_rest - price)
            sold = prev_hold + price
            rest = max(prev_rest, prev_sold)

        return max(sold, rest)