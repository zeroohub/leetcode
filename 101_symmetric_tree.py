# -*- coding: utf-8 -*-
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

class MySolution(object):
    """
    广度优先, 测每层是否对称
    """

    def check_last_level_balance(self):
        start_idx = self.current_index - self.current_level_num
        end_idx = self.current_index - 1
        while end_idx >= start_idx:
            if self.queue[start_idx][0] == self.queue[end_idx][0] == None:
                pass
            elif not (self.queue[start_idx][0] and self.queue[end_idx][0]):
                return False
            elif self.queue[start_idx][0].val != self.queue[end_idx][0].val:
                return False
            start_idx += 1
            end_idx -= 1
        return True

    def travel(self):
        if len(self.queue) == self.current_index:
            return self.check_last_level_balance()
        node, level = self.queue[self.current_index]
        if level > self.current_level:
            balance = self.check_last_level_balance()
            if not balance:
                return False
            self.current_level = level
            self.current_level_num = 0


        if node:
            self.queue.append((node.left, level+1))
            self.queue.append((node.right, level+1))

        self.current_level_num += 1
        return True

    def isSymmetric(self, root):
        self.current_level_num = 0
        self.current_level = 0
        self.queue = []
        self.current_index = 0

        self.queue.append((root, 1))
        while len(self.queue) >= self.current_index:
            if not self.travel():
                return False
            self.current_index += 1
        return True



