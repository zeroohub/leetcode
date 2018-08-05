# -*- coding: utf-8 -*-
class ListNode:

    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.pre = self.nex = None

    def __repr__(self) -> str:
        return str(self.val)


class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode(None, None)
        self.tail = ListNode(None, None)
        self.head.nex = self.tail
        self.tail.pre = self.head


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._append(node)
            return node.val

        return -1

    def _remove(self, node):
        pre = node.pre
        nex = node.nex
        pre.nex = nex
        nex.pre = pre

    def _append(self, node):
        tail = self.tail.pre
        tail.nex = node
        node.pre = tail
        node.nex = self.tail
        self.tail.pre = node

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self._remove(self.cache[key])
        node = ListNode(key, value)
        self._append(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            head = self.head.nex
            del self.cache[head.key]
            self._remove(head)
