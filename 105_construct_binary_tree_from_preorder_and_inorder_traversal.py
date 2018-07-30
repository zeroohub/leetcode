# -*- coding: utf-8 -*-
from data_structure import *

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34579/Python-short-recursive-solution.
        :param preorder:
        :param inorder:
        :return:
        """
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind + 1:])
            return root
