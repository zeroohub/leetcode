# -*- coding: utf-8 -*-
from data_structure import *


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        try:
            self.is_valid(root)
            return True
        except:
            return False



    def is_valid(self, root):
        left = right = root.val

        if root.left:
            left_min, left_max = self.is_valid(root.left)
            if root.val <= left_max:
                raise Exception

            left = left_min

        if root.right:
            right_min, right_max = self.is_valid(root.right)
            if root.val >= right_min:
                raise Exception

            right = right_max

        return (left, right)
