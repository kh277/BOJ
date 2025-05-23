# 백준 21920

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def GCD(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def solve(N, A, X):
    accSum = 0
    count = 0
    for i in range(N):
        if GCD(X, A[i]) == 1:
            accSum += A[i]
            count += 1

    return accSum/count


def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    print(solve(N, A, X))


main()
