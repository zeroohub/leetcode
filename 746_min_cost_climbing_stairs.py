# -*- coding: utf-8 -*-

class Solution:
    def minCostClimbingStairs(self, cost: 'List[int]') -> 'int':
        self.cache = {}
        return self.minCost(cost, len(cost))

    def minCost(self, cost, n):
        if n <= 1:
            return 0
        elif n in self.cache:
            return self.cache[n]

        n1 = self.minCost(cost, n-1) + cost[n-1]
        n2 = self.minCost(cost, n-2) + cost[n-2]
        result = min(n1, n2)
        self.cache[n] = result
        return result

class Solution:
    def minCostClimbingStairs(self, cost: 'List[int]') -> 'int':
        self.cache = {}
        cost.append(0)
        return self.minCost(cost, len(cost))


    def minCost(self, cost, n):
        n_1 = cost[1]
        n_2 = cost[0]
        for i in range(2, n):
            n_1, n_2 = min(n_1, n_2) + cost[i], n_1

        return n_1

def testSolution():
    for cost, result in [
        ([10, 15, 20], 15),
        ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6)
    ]:
        assert Solution().minCostClimbingStairs(cost) == result

testSolution()
