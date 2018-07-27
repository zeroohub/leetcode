# -*- coding: utf-8 -*-
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        TODO: kind of DFS or BFS
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.num = numCourses
        course2req = dict(prerequisites)
        taken = set()
        try:
            for c, r in prerequisites:
                self.take_course(c, course2req, taken)
        except:
            return False
        return True

    def take_course(self, course, c2r, taken):
        if course not in taken:
            self.num -= 1
            if self.num < 0:
                raise Exception
        if course not in c2r:
            taken.add(course)
            return 1
        else:
            r = c2r[course]
            result = 1 + self.take_course(r, c2r, taken)
            taken.add(course)
            c2r.pop(course)
            return result

print(Solution().canFinish(3, [[1,0],[2, 0]]))
