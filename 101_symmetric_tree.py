# -*- coding: utf-8 -*-
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    """
    TODO:
    广度优先, 测每层是否对称
    """
    def travel(self, node):
        if not node:
            return


    def isSymmetric(self, root):
        self.travel(root)
        """
        :type root: TreeNode
        :rtype: bool
        """
        pass
