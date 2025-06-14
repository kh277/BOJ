# 백준 13913

import io
from collections import deque
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 150000


def BFS(start, end):
    if start <= end:
        visited = array('i', [-1]) * INF
        q = deque()
        q.append([start, 0])
        visited[start] = start

        while q:
            curNum, curCount = q.popleft()

            if curNum == end:
                cur = end
                traceback = []
                while True:
                    if cur == start:
                        traceback.append(start)
                        break
                    traceback.append(cur)
                    cur = visited[cur]

                return [[curCount], traceback[::-1]]

            for nextNum in [curNum+1, curNum-1, curNum*2]:
                if 0 <= nextNum < INF and visited[nextNum] == -1:
                    q.append([nextNum, curCount+1])
                    visited[nextNum] = curNum

    else:
        return [[start-end], [i for i in range(start, end-1, -1)]]


def main():
    N, K = map(int, input().split())
    for i in BFS(N, K):
        print(*i)


main()
