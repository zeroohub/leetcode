# -*- coding: utf-8 -*-
class MySolution(object):
    def maxProfit(self, prices):
        """
        iterate over possible situation, bad solution
        time exceeded.
        :type prices: List[int]
        :rtype: int
        """
        self.max_profit = 0
        self.action(0, 'cooldown', 0, prices)
        return self.max_profit

    def action(self, profit, last_action, stock_left, prices):
        if profit > self.max_profit:
            self.max_profit = profit

        if not prices:
            return

        price = prices[0]
        if stock_left:
            self.action(profit+price, 'sell', 0, prices[1:])
            self.action(profit, 'cooldown', 1, prices[1:])
        else:
            if last_action == 'sell':
                self.action(profit, 'cooldown', 0, prices[1:])
            elif last_action == 'cooldown':
                self.action(profit-price, 'buy', 1, prices[1:])
                self.action(profit, 'cooldown', 0, prices[1:])

class Solution2(object):
    def maxProfit(self, prices):
        """
        good DP solution from discuss
        https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75927/Share-my-thinking-process

        buy(i) = max(buy(i-1), sell(i-2)-price)
        sell(i) = max(sell(i-1), buy(i-1)+price)
        """
        if len(prices) < 2:
            return 0

        buy, sell, pre_buy, pre_sell = -prices[0], 0, 0, 0

        for price in prices:
            pre_buy = buy
            buy = max(buy, pre_sell - price)
            pre_sell = sell
            sell = max(sell, pre_buy + price)

        return max(buy, sell)
