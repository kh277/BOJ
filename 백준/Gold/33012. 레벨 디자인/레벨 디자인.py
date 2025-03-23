# 백준 33012

'''
짝수 : 1 2 / 4 3 / 5 6 / 8 7  : 증가 감소 번갈아가며
홀수 : 1 2 / 4 3 / 5 6 / 7 9 8  : 증가 감소 번갈아가면 하다 마지막 3개만 다르게 
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def checker(N, num):

    DP = [0 for _ in range(N)]
    DP[0] = num[0]
    DP[1] = num[1]
    DP[2] = num[0] + num[2]

    for i in range(3, N):
        DP[i] = max(DP[i-3], DP[i-2]) + num[i]

    return [max(DP[N-1], DP[N-2])]


def solve(N):
    if N < 3:
        return [[1, 2][:N], [N]]

    result = [0 for _ in range(N)]

    for i in range(N%2, N-1, 2):
        if i % 4 == 0 or i % 4 == 3:
            result[i] = i+1
            result[i+1] = i+2
        else:
            result[i] = i+2
            result[i+1] = i+1

    if N % 2 == 1:
        result[0] = 1

    return [result, checker(N, result)]


def main():
    N = int(input())
    for i in solve(N):
        print(*i)


main()