# 백준 1717

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def find(parent, x):
    root = x
    while parent[root] >= 0:
        root = parent[root]
    
    while x != root:
        nextN = parent[x]
        parent[x] = root
        x = nextN

    return root


def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)

    if x == y:
        return

    if parent[x] > parent[y]:
        parent[x] = y
    else:
        if parent[x] == parent[y]:
            parent[x] -= 1
        parent[y] = x


def main():
    N, M = map(int, input().split())
    parent = array('i', [-1]) * (N+1)
    for _ in range(M):
        q, a, b = map(int, input().split())
        if q == 0:
            union(parent, a, b)
        else:
            if find(parent, a) == find(parent, b):
                print("YES")
            else:
                print("NO")


main()
