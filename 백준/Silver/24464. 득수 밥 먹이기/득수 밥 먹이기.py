# 백준 24464

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
MOD = 1000000007


def solve(N):
    prevDP = [1, 1, 1, 1, 1]

    for _ in range(1, N):
        curDP = [(prevDP[1] + prevDP[2] + prevDP[3] + prevDP[4]) % MOD,
                (prevDP[0] + prevDP[3] + prevDP[4]) % MOD,
                (prevDP[0] + prevDP[4]) % MOD,
                (prevDP[0] + prevDP[1]) % MOD,
                (prevDP[0] + prevDP[1] + prevDP[2]) % MOD]
        prevDP = curDP

    return sum(prevDP) % MOD


def main():
    N = int(input())
    print(solve(N))


main()
