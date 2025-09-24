# 백준 5670

'''
참고한 구현체 : https://justicehui.github.io/medium-algorithm/2019/03/28/LCA/
'''

import io
import math

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
ARRAY_TYPE = 'I'


class LCA():
    def __init__(self, N, graph, root):
        self.N = N
        self.LOG = math.ceil(math.log2(N)) + 1
        self.graph = graph
        self.depth = [0] * (N+1)
        self.DP = [[0] * self.LOG for _ in range(N+1)]

        self.DFS(root)
        self.calDP()


    # 각 정점별 depth 계산
    def DFS(self, root):
        visited = [0] * (self.N+1)

        stack = []
        stack.append([root, 0])
        self.depth[root] = 0
        visited[root] = 1

        while stack:
            curV, curDepth = stack.pop()

            for nextV in self.graph[curV]:
                if visited[nextV] == 0:
                    self.DP[nextV][0] = curV
                    self.depth[nextV] = curDepth+1
                    visited[nextV] ^= 1
                    stack.append([nextV, curDepth+1])


    # DP 테이블 채우기
    def calDP(self):
        for x in range(1, self.LOG):
            for y in range(1, self.N+1):
                self.DP[y][x] = self.DP[self.DP[y][x-1]][x-1]


    # LCA 계산
    def LCA(self, startV, endV):
        if self.depth[startV] < self.depth[endV]:
            startV, endV = endV, startV

        gap = self.depth[startV] - self.depth[endV]
        index = 0
        while gap:
            if gap & 1:
                startV = self.DP[startV][index]
            gap >>= 1
            index += 1

        if startV == endV:
            return startV

        for i in range(self.LOG-1, -1, -1):
            if self.DP[startV][i] != self.DP[endV][i]:
                startV = self.DP[startV][i]
                endV = self.DP[endV][i]

        return self.DP[startV][0]


def main():
    N = int(input())
    root = 1
    graph = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    lca = LCA(N, graph, root)

    M = int(input())
    for _ in range(M):
        a, b = map(int, input().split())
        print(lca.LCA(a, b))


main()
