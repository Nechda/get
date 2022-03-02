#!/usr/bin/python
from collections import defaultdict
class Tree:
    def empty_init(self, n : int):
        self.n = n
        self.dict = defaultdict(set)
    def __init__(self, pruffer : list):
        self.empty_init(len(pruffer) + 2)
        vertices = [i for i in range(self.n)]
        while len(pruffer):
            for num, i in enumerate(vertices):
                if i not in pruffer:
                    self.insert_edge(i, pruffer[0])
                    del vertices[num]
                    break
            del pruffer[0]
        self.insert_edge(vertices[0], vertices[1])

    def insert_edge(self, i, j):
        assert(i < self.n and j < self.n)
        self.dict[i].add(j)
        self.dict[j].add(i)

    def height(self, node = 0):
        return self._height(node, -1)

    def _height(self, node, parent):
        ret = -1
        for i in self.dict[node]:
            if i != parent:
                ret = max(ret, self._height(i, node))
        return ret + 1
    def to_dot(self):
        s = "strict graph {\n"
        for i in self.dict:
            for j in self.dict[i]:
                s += "{} -- {}\n".format(i, j)
        s += "}"
        return s
