# -*- coding: utf-8 -*-
from data_structure import *

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxi = root.val
        self.traversal(root)
        return self.maxi

    def traversal(self, node):
        if not node:
            return 0

        left = self.traversal(node.left)
        right = self.traversal(node.right)
        self.maxi = max(node.val + left + right, self.maxi)
        ret = max(left, right) + node.val
        return max(ret, 0)

print(Solution().maxPathSum(stringToTreeNode('[1, 2, 3]')))
