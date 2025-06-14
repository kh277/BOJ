# 백준 13913

import io
from collections import deque
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 150000


def BFS(start, end):
    if start <= end:
        visited = array('i', [0]) * INF
        q = deque()
        q.append([start, 0, [start]])
        visited[start] = 1

        while q:
            curNum, curCount, curVisit = q.popleft()

            if curNum == end:
                return [[curCount], curVisit]

            for nextNum in [curNum+1, curNum-1, curNum*2]:
                if 0 <= nextNum < INF and visited[nextNum] == 0:
                    q.append([nextNum, curCount+1, curVisit + [nextNum]])
                    visited[nextNum] = 1

    else:
        return [[start-end], [i for i in range(start, end-1, -1)]]


def main():
    N, K = map(int, input().split())
    for i in BFS(N, K):
        print(*i)


main()
