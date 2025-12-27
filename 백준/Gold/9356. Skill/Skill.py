# 백준 9356

'''
DP[i][j] = i자리 정수 중 마지막 자리의 숫자가 j인 비내림차순 수의 개수
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
MOD = 1000000007


def init():
    DP = [[0] * 19 for _ in range(100001)]
    for i in range(10):
        DP[0][i] = 0
        DP[1][i] = 1

    for i in range(2, 100001):
        for j in range(10):
            DP[i][j] = (DP[i-1][j] + DP[i][j-1]) % MOD

    return DP


def main():
    DP = init()

    T = int(input())
    for _ in range(T):
        N = int(input())
        print(sum(DP[N]) % MOD)


main()
