# -*- coding: utf-8 -*-
from data_structure import *
class Solution(object):
    def detectCycle(self, head):
        """
        TODO
        :type head: ListNode
        :rtype: ListNode
        """

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow

        return None

print(Solution().detectCycle(stringToListNode('[3,2,0,-4]')))
