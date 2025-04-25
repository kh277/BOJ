# 백준 7239

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, A):
    A.sort()
    mid = N//2
    result = []
    for i in range(mid):
        result.append(A[mid+i])
        result.append(A[i])
    if N % 2 == 1:
        result.append(A[N-1])

    return result


def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(*solve(N, A))


main()
