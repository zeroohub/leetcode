# -*- coding: utf-8 -*-
from data_structure import *

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.traversal(root)

    def traversal(self, root):
        if not root.left and not root.right:
            return root

        left_end = root
        if root.left:
            left_end = self.traversal(root.left)

        temp = root.right
        root.right = root.left
        root.left = None
        left_end.right = temp
        right_end = left_end
        if temp:
            right_end = self.traversal(temp)
        return right_end


