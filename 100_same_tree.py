# -*- coding: utf-8 -*-
from data_structure import *

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True

        elif not p or not q:
            return False

        p_queue = [p]
        q_queue = [q]

        while p_queue and q_queue:
            pnode = p_queue[0]
            qnode = q_queue[0]

            pval = pnode.val if pnode else None
            qval = qnode.val if qnode else None

            if pval != qval:
                return False

            if qval == qval is not None:

                p_queue.append(pnode.left)
                p_queue.append(pnode.right)

                q_queue.append(qnode.left)
                q_queue.append(qnode.right)

            p_queue = p_queue[1:]
            q_queue = q_queue[1:]
        return True
