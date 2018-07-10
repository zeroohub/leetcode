# -*- coding: utf-8 -*-
from data_structure import *

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.result = []
        self.travel(root)
        return self.result

    def travel(self, root):
        if not root:
            return

        self.travel(root.left)
        self.result.append(root.val)
        self.travel(root.right)


class Solution2(object):
    """
    iterative solution with stack
    """
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.result = []
        self.travel([root])
        return self.result

    def travel(self, stack):
        while len(stack) > 0:
            node = stack[-1]
            if node.left:
                stack.append(node.left)
                node.left = None
                continue
            node = stack.pop()
            self.result.append(node.val)
            if node.right:
                stack.append(node.right)
                continue




print(Solution2().inorderTraversal(stringToTreeNode('[1,null,2,3]')))
