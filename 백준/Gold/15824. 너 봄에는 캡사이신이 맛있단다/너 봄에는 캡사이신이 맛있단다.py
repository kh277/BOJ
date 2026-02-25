# 백준 15824

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
MOD = 1000000007


def solve(N, A):
    A.sort()
    result = 0
    accSum = 0
    startI = 0
    endI = N-1
    for i in range(1, N):
        accSum += A[endI] - A[startI]
        result = (result + pow(2, i-1, MOD) * accSum) % MOD
        startI += 1
        endI -= 1

    return result


def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))


main()
