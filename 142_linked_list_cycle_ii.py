# -*- coding: utf-8 -*-
class Solution(object):
    def detectCycle(self, head):
        """
        TODO
        :type head: ListNode
        :rtype: ListNode
        """

        slow = fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next.next
