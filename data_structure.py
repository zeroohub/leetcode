# -*- coding: utf-8 -*-

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
