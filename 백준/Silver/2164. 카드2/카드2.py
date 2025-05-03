# 백준 2164

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N):
    q = deque([i for i in range(1, N+1)])

    for _ in range(N-1):
        q.popleft()
        q.append(q.popleft())

    return q.popleft()


def main():
    N = int(input())
    print(solve(N))


main()
