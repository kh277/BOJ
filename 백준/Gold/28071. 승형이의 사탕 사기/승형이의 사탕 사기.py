# 백준 28071

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def BFS(N, M, K, candy):
    visited = set()
    q = deque()
    q.append([0, 0])
    visited.add(0)
    result = 0

    while q:
        curBox, curCandy = q.popleft()
        if curCandy % K == 0:
            result = max(result, curCandy)

        if curBox == M:
            continue

        for addCandy in candy:
            nextCandy = curCandy+addCandy
            if nextCandy not in visited:
                q.append([curBox+1, nextCandy])
                visited.add(nextCandy)

    return result


def main():
    N, M, K = map(int, input().split())
    candy = list(map(int, input().split()))
    print(BFS(N, M, K, candy))


main()
