# 백준 14725

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


class Trie:
    def __init__(self):
        self.root = dict()

    def add(self, value):
        curV = self.root
        for v in value:
            if v not in curV:
                curV[v] = dict()
            curV = curV[v]
        curV[0] = True

    def DFS(self, level, curV):
        if 0 in curV:
            return
        nextV = sorted(curV)
        for v in nextV:
            print("--"*level + v)
            self.DFS(level+1, curV[v])


def main():
    N = int(input())
    trie = Trie()
    for _ in range(N):
        _, *data = input().decode().split()
        trie.add(data)
    trie.DFS(0, trie.root)


main()
