# -*- coding: utf-8 -*-
from data_structure import *

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.traversing(root)
        return root

    def traversing(self, node):
        if not node:
            return
        if node.left == node.right is None:
            return

        temp = node.left
        node.left = node.right
        node.right = temp
        self.traversing(node.left)
        self.traversing(node.right)
