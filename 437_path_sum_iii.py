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


