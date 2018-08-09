# -*- coding: utf-8 -*-
import heapq
class Solution:
    def getSkyline(self, buildings):
        """
        TODO
        https://briangordon.github.io/2014/08/the-skyline-problem.html
        https://leetcode.com/problems/the-skyline-problem/discuss/61261/10-line-Python-solution-104-ms
        :param buildings:
        :return:
        """
        events = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, None) for _, R, _ in buildings}))
        res, hp = [[0, 0]], [(0, float("inf"))]
        for x, negH, R in events:
            while x >= hp[0][1]:
                heapq.heappop(hp)
            if negH:
                heapq.heappush(hp, (negH, R))
            if res[-1][1] + hp[0][0]:
                res += (x, -hp[0][0]),
        return res[1:]


assert Solution().getSkyline([[2,9,10], [3,7,15], [5,12,12], [15,20,10], [19,24,8]]) == [(2, 10), (3, 15), (7, 12), (12, 0), (15, 10), (20, 8), (24, 0)]
assert Solution().getSkyline([[3,10,20],[3,9,19],[3,8,18],[3,7,17],[3,6,16],[3,5,15],[3,4,14]]) == [(3, 20), (10, 0)]
assert Solution().getSkyline([[0,2,3], [2,5,3]]) == [(0, 3), (5, 0)]
assert Solution().getSkyline([[1,2,1],[1,2,2],[1,2,3]]) == [(1, 3), (2, 0)]
