# -*- coding: utf-8 -*-
from data_structure import *

class Solution(object):
    """
    same DP solution, just add width first traversing
    ERROR: misunderstand question, result error
    f(1) = root.val
    f(2) = max(root.val, f(root.left) + f(root.right))
    f(3) = max(root.val+f())
    """
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        pre, curr = self.traversing(root)
        return curr

    def traversing(self, root):
        if not root:
            return 0, 0

        right_pre, right_curr = self.traversing(root.right)
        left_pre, left_curr = self.traversing(root.left)

        curr = root.val + right_pre + left_pre
        pre = right_curr + left_curr
        return pre, max(curr, pre)

print(Solution().rob(stringToTreeNode('[3,2,3,null,3,null,1]')))
