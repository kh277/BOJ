# 백준 16565

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
MOD = 10007


def initComb():
    DP = [[0] * 53 for _ in range(53)]

    for i  in range(53):
        for j in range(i+1):
            if i == j or j == 0:
                DP[i][j] = 1
            else:
                DP[i][j] = (DP[i-1][j-1] + DP[i-1][j]) % MOD

    return DP


def solve(N):
    DP = initComb()

    result = 0
    for i in range(1, N//4+1):
        if i & 1:
            result += (DP[13][i] * DP[52-(i<<2)][N-(i<<2)]) % MOD
            result = result % MOD
        else:
            result -= (DP[13][i] * DP[52-(i<<2)][N-(i<<2)]) % MOD
            result = (result + MOD) % MOD

    return result


def main():
    N = int(input())
    print(solve(N))


main()
