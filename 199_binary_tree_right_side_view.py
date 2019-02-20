# -*- coding: utf-8 -*-
from data_structure import TreeNode

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.result = []

        self.dfs(root, 0)
        return self.result

    def dfs(self, node, idx):
        if not node:
            return
        if idx == len(self.result):
            self.result.append(node.val)
        else:
            self.result[idx] = node.val

        self.dfs(node.left, idx + 1)
        self.dfs(node.right, idx + 1)
