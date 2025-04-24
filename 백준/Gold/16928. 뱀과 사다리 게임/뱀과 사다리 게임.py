# 백준 16928

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
point = [1, 2, 3, 4, 5, 6]


def BFS(ladder, snake):
    visited = [False for _ in range(101)]

    q = deque()
    q.append([1, 0])
    visited[1] = True

    while q:
        curV, curCount = q.popleft()
        if curV == 100:
            return curCount

        for i in range(6):
            nextV = curV + point[i]
            if nextV <= 100 and visited[nextV] == False:
                if nextV in ladder:
                    if visited[ladder[nextV]] == False:
                        visited[ladder[nextV]] = True
                    q.append([ladder[nextV], curCount+1])
                elif nextV in snake:
                    if visited[snake[nextV]] == False:
                        visited[snake[nextV]] = True
                    q.append([snake[nextV], curCount+1])
                else:
                    q.append([nextV, curCount+1])
                
                visited[nextV] = True


def main():
    N, M = map(int, input().split())
    ladder = dict()
    for _ in range(N):
        a, b = list(map(int, input().split()))
        ladder[a] = b

    snake = dict()
    for _ in range(M):
        a, b = list(map(int, input().split()))
        snake[a] = b

    print(BFS(ladder, snake))


main()
