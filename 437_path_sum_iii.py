# -*- coding: utf-8 -*-
from collections import defaultdict
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class MySolution(object):
    def pathSum(self, root, total):
        """
        :type root: TreeNode
        :type total: int
        :rtype: int
        """
        self.counter = 0
        self.total = total
        self.checkSum(root, defaultdict(int))
        return self.counter

    def checkSum(self, node, current_totals):
        if not node:
            return
        else:
            next_totals = defaultdict(int)
            for val, cnt in current_totals.iteritems():
                new_val = val + node.val
                next_totals[new_val] = cnt
                if new_val == self.total:
                    self.counter += cnt

            if node.val == self.total:
                self.counter += 1
            next_totals[node.val] += 1

            self.checkSum(node.left, next_totals)
            self.checkSum(node.right, next_totals)



class Solution2(object):
    def pathSum(self, root, target):
        cache = defaultdict(int, {0: 1})
        self.result = 0
        self.dfs(root, target, 0, cache)
        return self.result

    def dfs(self, node, target, current_sum, cache):
        if not node:
            return
        current_sum += node.val
        old_sum = current_sum - target
        self.result += cache[old_sum]
        cache[current_sum] += 1
        self.dfs(node.left, target, current_sum, cache)
        self.dfs(node.right, target, current_sum, cache)
        cache[current_sum] -= 1
