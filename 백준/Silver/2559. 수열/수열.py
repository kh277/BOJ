# 백준 2559

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, K, A):
    accSum = sum([A[i] for i in range(K)])
    result = accSum
    right = K

    while right < N:
        accSum += A[right] - A[right-K]
        result = max(result, accSum)
        right += 1

    return result


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    print(solve(N, K, A))


main()
