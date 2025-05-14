# 백준 13703

'''
DP[i][j] = i초 후 물벼룩이 높이 jcm에 있을 경우의 수
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
move = [-1, 1]


def solve(K, N):
    if K - 3*N > 0:
        return 0

    DP = [[0 for _ in range(K+3*N+1)] for _ in range(N+1)]
    DP[0][K] = 1

    for t in range(N):
        for curH in range(1, K+3*N+1):
            if DP[t][curH] == 0:
                continue
            for dH in move:
                nextH = curH + dH
                if nextH <= 0:
                    nextH = 0
                DP[t+1][nextH] += DP[t][curH]

    return sum(DP[N]) - DP[N][0]


def main():
    K, N = map(int, input().split())
    print(solve(K, N))


main()
