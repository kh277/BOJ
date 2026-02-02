# 백준 22653

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, A):
    A.sort()

    accSum = 0
    for i in range(N):
        if accSum+1 < A[i]:
            break
        accSum += A[i]

    return accSum+1


def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))


main()
