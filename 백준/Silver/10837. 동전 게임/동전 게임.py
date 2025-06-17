# 백준 10837

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(K, M, N):
    leftRound = K - max(M, N)
    gap = abs(M-N) - leftRound
    if M > N and gap <= 2:
        return 1
    elif M < N and gap <= 1:
        return 1
    elif M == N:
        return 1
    return 0


def main():
    K = int(input())
    C = int(input())
    for _ in range(C):
        M, N = map(int, input().split())
        print(solve(K, M, N))


main()
