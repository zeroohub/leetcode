# -*- coding: utf-8 -*-
import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._list = []
        self._map = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self._map:
            return False
        self._map[val] = len(self._list)
        self._list.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self._map:
            return False
        idx = self._map[val]
        self._map[self._list[-1]] = idx
        del self._map[val]
        self._list[idx], self._list[-1] = self._list[-1], self._list[idx]
        self._list.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self._list)

s = RandomizedSet()
s.insert(0)
s.remove(0)
s.insert(-1)
s.remove(0)
print(s.getRandom())
