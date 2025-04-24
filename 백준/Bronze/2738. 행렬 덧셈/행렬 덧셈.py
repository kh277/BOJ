# 백준 2738

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, M, A, B):
    for y in range(N):
        for x in range(M):
            A[y][x] += B[y][x]
    
    return A


def main():
    N, M = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
    B = []
    for _ in range(N):
        B.append(list(map(int, input().split())))
    
    for i in solve(N, M, A, B):
        print(*i)


main()
