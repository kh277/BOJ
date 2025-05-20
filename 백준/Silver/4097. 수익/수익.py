# 백준 4097

'''
DP[i] = 구간 [0, i]에서의 최대 연속합
'''

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**10


def solve(N, A):
    result = -INF
    DP = array('i', [0]) * N
    DP[0] = A[0]
    for i in range(1, N):
        DP[i] = max(A[i], DP[i-1]+A[i])
        result = max(result, DP[i])

    return result


def main():
    while True:
        N = int(input())
        if N == 0:
            break
        A = array('i')
        for _ in range(N):
            A.append(int(input()))
        print(solve(N, A))


main()
