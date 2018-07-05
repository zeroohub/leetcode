# -*- coding: utf-8 -*-
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        best_profit = 0
        current_minimum = prices[0]

        for i in prices:
            current_minimum = min(i, current_minimum)
            profit = i - current_minimum
            if profit > best_profit:
                best_profit = profit
        return best_profit

