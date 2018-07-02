# -*- coding: utf-8 -*-

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
        self.checkSum(root, [])
        return self.counter

    def checkSum(self, node, current_totals):
        if not node:
            return
        else:
            next_totals = []
            for t in current_totals:
                nt = t + node.val
                next_totals.append(nt)
                if nt == self.total:
                    self.counter += 1
            if node.val == self.total:
                self.counter += 1
            next_totals.append(node.val)

            self.checkSum(node.left, next_totals)
            self.checkSum(node.right, next_totals)


