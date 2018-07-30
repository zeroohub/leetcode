# -*- coding: utf-8 -*-
from collections import defaultdict


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        DFS solution
        :param numCourses:
        :param prerequisites:
        :return:
        """
        self.starts = defaultdict(list)
        self.added = set()
        self.temp = set()
        for c, d in prerequisites:
            self.starts[d].append(c)

        for fnode, tnode in self.starts.items():
            try:
                self.dfs(fnode, tnode)
            except:
                return False

        return len(self.added) <= numCourses

    def dfs(self, fnode, tnode):
        if fnode in self.added:
            return
        if fnode in self.temp:
            raise Exception

        self.temp.add(fnode)
        for tn in tnode:
            if tn in self.starts:
                self.dfs(tn, self.starts[tn])
            else:
                self.added.add(tn)
        self.temp.remove(fnode)
        self.added.add(fnode)



print(Solution().canFinish(2, [[1,2],[2, 0]]))
