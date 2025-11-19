# 백준 1409

import io
import math
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
dx = [-1, 1]


def BFS(N, setP, visited, start, theta):
    result = 0
    q = deque()
    q.append(start)
    visited.add(start)

    while q:
        curV = q.popleft()

        for i in range(2):
            nextV = curV + theta*dx[i]
            if nextV < 0:
                nextV += 360
            elif nextV >= 360:
                nextV -= 360

            if nextV in setP and nextV not in visited:
                q.append(nextV)
                visited.add(nextV)
                result += 1

    return result


def solve(N, point):
    if N == 1:
        return 0

    # 두 점 사이의 간격 전부 구하기
    result = 0
    point.sort()
    gap = []
    for i in range(N-1):
        for j in range(i+1, N):
            gap.append(point[j]-point[i])

    # 회전각이 theta일 때, 이어질 수 있는 간선의 총 개수를 구하기
    setP = set(point)
    for theta in gap:
        visited = set()
        curRes = 0
        for i in range(N):
            if point[i] not in visited:
                curRes += math.ceil(BFS(N, setP, visited, point[i], theta)/2) * 2

        result = max(result, curRes)

    return result


def main():
    N = int(input())
    point = []
    for _ in range(N):
        point.append(int(input()))

    print(solve(N, point))


main()
