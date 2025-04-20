# 백준 2003

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, M, A):
    accSum = [0 for _ in range(N)]
    accSum[0] = A[0]

    for i in range(1, N):
        accSum[i] = accSum[i-1] + A[i]

    result = 0
    for i in range(N):
        if accSum[i] == M:
            result += 1

    for left in range(N):
        for right in range(left, N):
            if accSum[right] - accSum[left] == M: 
                result += 1

    return result


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    print(solve(N, M, A))


main()
