# 백준 2003

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, M, A):
    left = 0
    right = 0
    accSum = A[0]
    result = 0

    while right < N:
        if accSum < M:
            right += 1
            if right == N:
                break
            accSum += A[right]
        elif accSum > M:
            accSum -= A[left]
            left += 1
        else:
            result += 1
            right += 1
            if right == N:
                break
            accSum += A[right]

    return result


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    print(solve(N, M, A))


main()
