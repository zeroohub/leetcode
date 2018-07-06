# -*- coding: utf-8 -*-
from data_structure import *

class MySolution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        self.traversing(root, 0)
        return root

    def traversing(self, node, big_val):
        if not node.right and not node.left:
            node.val += big_val
            return node.val
        if node.right:
            node.val += self.traversing(node.right, big_val)
        else:
            node.val += big_val

        if node.left:
            return self.traversing(node.left, node.val)

        return node.val



class Solution2(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.total = 0

        def traverse(root):
            if not root:
                return root
            traverse(root.right)
            root.val += self.total
            self.total = root.val
            traverse(root.left)

        traverse(root)
        return root
