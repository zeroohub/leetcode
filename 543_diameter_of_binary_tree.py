# -*- coding: utf-8 -*-
class MySolution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_diameter = 0
        self.tree_depth(root)
        return self.max_diameter

    def tree_depth(self, node):
        if not node:
            return 0
        left_tree_depth = self.tree_depth(node.left)
        right_tree_depth = self.tree_depth(node.right)
        diameter = left_tree_depth + right_tree_depth
        self.max_diameter = max(diameter, self.max_diameter)
        return 1 + max(left_tree_depth, right_tree_depth)
