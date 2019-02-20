# -*- coding: utf-8 -*-
from data_structure import *
from collections import defaultdict

class Solution(object):
    def copyRandomList(self, head):
        cache = defaultdict(list)
        result_head = new_head = RandomListNode(0)
        temp_head = head
        while head:
            new_node = RandomListNode(head.label)
            new_head.next = new_node
            new_head = new_head.next
            if head.random:
                cache[head.random].append(new_node)
            head = head.next

        head = temp_head
        new_head = result_head.next
        while head:
            if head in cache:
                for node in cache[head]:
                    node.random = new_head
            head = head.next
            new_head = new_head.next
        return result_head.next



class Solution(object):
    def __init__(self):
        self.cloned = {}
    def copyRandomList(self, head):

        if not head:
            return

        if head in self.cloned:
            return self.cloned[head]

        node = RandomListNode(head.label)
        self.cloned[head] = node
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node


class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        temp_head = head

        while head:
            node = RandomListNode(head.label)
            node.next = head.next
            head.next = node
            head = node.next

        head = temp_head
        while head:
            if head.random:
                node = head.next
                node.random = head.random.next

            head = head.next.next

        head = temp_head
        new_head = head.next
        while head:
            node = head.next
            head.next = node.next
            head = head.next
            node.next = head.next if head else None

        return new_head
