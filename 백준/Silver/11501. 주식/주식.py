# 백준 11501

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, A):
    prevMax = A[N-1]
    total = 0
    for i in range(N-2, -1, -1):
        if prevMax > A[i]:
            total += prevMax - A[i]
        else:
            prevMax = A[i]

    return total


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        print(solve(N, A))


main()
