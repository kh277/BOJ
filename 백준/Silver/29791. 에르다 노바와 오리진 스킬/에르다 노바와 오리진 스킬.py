# 백준 29791

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, M, A, B):
    A.sort()
    B.sort()

    countA = 0
    curT = 0
    for i in range(N):
        if A[i] >= curT:
            countA += 1
            curT = A[i] + 100

    countB = 0
    curT = 0
    for i in range(M):
        if B[i] >= curT:
            countB += 1
            curT = B[i] + 360
    
    return [countA, countB]


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(*solve(N, M, A, B))


main()
