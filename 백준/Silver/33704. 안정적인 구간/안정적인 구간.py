# 백준 33074

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, A):
    for i in range(N-1):
        if A[i] <= A[i+1]:
            return 'YES'

    for i in range(N-2):
        if A[i+2] <= A[i+1] <= A[i]:
            return 'YES'

    return 'NO'


def main():
    N = int(input())
    A = list(map(int, input().split()))

    print(solve(N, A))


main()
