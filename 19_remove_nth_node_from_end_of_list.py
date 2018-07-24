# -*- coding: utf-8 -*-
from data_structure import *

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        there are other solution like `slow/fast pointer`, two pointer seperate by n
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        if not head:
            return None

        queue = []
        ohead = head
        while head:
            queue.append(head)
            if len(queue) > n + 1:
                queue.pop(0)

            head = head.next


        idx = -n
        prev_idx = idx-1
        next_idx = idx+1

        lq = len(queue)
        if lq >= abs(prev_idx) and next_idx < 0:
            queue[prev_idx].next = queue[next_idx]
            return ohead
        if lq < abs(prev_idx) and next_idx < 0:
            return queue[next_idx]
        if lq >= abs(prev_idx) and next_idx >= 0:
            queue[prev_idx].next = None
            return ohead
        if lq < abs(prev_idx) and next_idx >= 0:
            return None


print(Solution().removeNthFromEnd(stringToListNode('[1]'), 1))
