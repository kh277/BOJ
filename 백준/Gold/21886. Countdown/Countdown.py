# 백준 21866

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, S, arr):
    accSum = [0] * N
    accSum[0] = arr[0]
    for i in range(1, N):
        accSum[i] = accSum[i-1] + arr[i]

    for i in range(1, N+1):
        temp = S + accSum[i-1]
        if temp % i == 0:
            result = temp // i
            if i < N and arr[i] > result:
                return result

    return result


def main():
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solve(N, S, arr))


main()
