# -*- coding: utf-8 -*-
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class MySolution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        object_ids = set()
        while head:
            oid = id(head)
            if oid in object_ids:
                return True
            else:
                object_ids.add(oid)
                head = head.next
        return False


class Solution2(object):
    """
    fast slow pointer, imagine two runner running on a track,
    one of them is fast, another is slow.
    if track is circle, fast will meet slow at some point
    """
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
