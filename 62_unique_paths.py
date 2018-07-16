# -*- coding: utf-8 -*-

class MySolution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.pathes = []
        self.travel([], 1, 1, m, n)
        return len(self.pathes)

    def travel(self, path, i, j, i_max, j_max):
        if i == i_max and j == j_max:
            self.pathes.append(path + [(i, j)])
            return

        if i < i_max:
            self.travel(path + [(i, j)], i+1, j, i_max, j_max)
        if j < j_max:
            self.travel(path + [(i, j)], i, j+1, i_max, j_max)



class MySolution2(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.pathes = [[0 for i in range(m)]for i in range(n)]
        for row in range(n):
            for col in range(m):
                if col == 0 or row == 0:
                    self.pathes[row][col] = 1
                else:
                    self.pathes[row][col] = self.pathes[row-1][col] + self.pathes[row][col-1]

        return self.pathes[n-1][m-1]
