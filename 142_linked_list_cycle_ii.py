# -*- coding: utf-8 -*-
from data_structure import *
# HARD
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        meet = None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                meet = True
                break

        if meet:
            fast = head
            while fast != slow:
                fast = fast.next
                slow = slow.next

        return meet and slow

print(Solution().detectCycle(stringToListNode('[3,2,0,-4]')))
