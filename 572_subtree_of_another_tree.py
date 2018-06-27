# -*- coding: utf-8 -*-
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class MySolution(object):
    """
    iterate through node, compare if the current subtree equal to given tree
    """
    def isSameTree(self, s, t):
        if s == t is None:
            return True
        if not (isinstance(s, TreeNode) and isinstance(t, TreeNode)):
            return False
        if s.val == t.val and self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right):
            return True
        return False

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if self.isSameTree(s, t):
            return True
        if not (isinstance(s, TreeNode) and isinstance(t, TreeNode)):
            return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

class Solution2(object):
    """
    build preorder string, than compare substring
    """

    def pre_order_tree(self, t, result=None):
        if not result:
            result = []
        result.append("#{}".format(t.val))
        if not t.left:
            result.append('lnull')
        else:
            self.pre_order_tree(t.left, result)

        if not t.right:
            result.append('rnull')
        else:
            self.pre_order_tree(t.right, result)
        return result

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        spre_str = " ".join(self.pre_order_tree(s))
        tpre_str = " ".join(self.pre_order_tree(t))
        return tpre_str in spre_str
