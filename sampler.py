#!/usr/bin/python
from trees import Tree
from sys import argv
from random import randrange

def generate_pruffer(n):
    return [randrange(n) for i in range(n - 2)]

def generate_tree(n, h):
    if h < 1 or n < 1:
        return None
    t = None
    while True:
        pruffer = generate_pruffer(n)
        t = Tree(pruffer)
        if t.height() <= h:
            break

    return t


n = int(argv[1])
h = int(argv[2])

print(generate_tree(n, h).to_dot())
