# -*- coding: utf-8 -*-
from data_structure import *

class Solution(object):
    def flatten(self, root):
        """
        TODO
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        print(self.traversal(root))

    def traversal(self, root):
        if root:
            result = [root.val]
            if root.left:
                result += self.traversal(root.left)
            if root.right:
                result += self.traversal(root.right)
            return result
