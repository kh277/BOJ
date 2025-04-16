# 백준 1717

import io
from array import array
import sys

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
sys.setrecursionlimit(10**5)


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    parent[max(a, b)] = min(a, b)


def main():
    N, M = map(int, input().split())
    parent = array('I', range(N+1))
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
    