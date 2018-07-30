# -*- coding: utf-8 -*-
from data_structure import *

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        mid = preorder[0]
        node = TreeNode(mid)
        inorder.index(mid)
