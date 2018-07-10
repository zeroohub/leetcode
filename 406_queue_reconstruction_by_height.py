# -*- coding: utf-8 -*-
class Solution(object):
    """
    fail to come up with a good solution myself
    below is a good solution coming from network:
    https://leetcode.com/problems/queue-reconstruction-by-height/discuss/89359/Explanation-of-the-neat-Sort+Insert-solution

    """
    def reconstructQueue(self, people):
        people.sort(key=lambda p: (-p[0], p[1]))
        queue = []
        for p in people:
            queue.insert(p[1], p)
        return queue
