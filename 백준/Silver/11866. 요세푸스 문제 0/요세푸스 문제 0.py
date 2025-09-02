# 백준 11866

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, K):
    q = deque([i for i in range(1, N+1)])
    result = ["<"]

    while q:
        for _ in range(K-1):
            cur = q.popleft()
            q.append(cur)
        result.append(str(q.popleft()))
        result.append(", ")
    result.pop()
    result.append(">")
    
    return ''.join(result)


def main():
    N, K = map(int, input().split())
    print(solve(N, K))


main()
