# 백준 2673

'''
DP[i][j] = 구간 [i, j] 내에서 잡을 수 있는 서로 교차하지 않는 현의 최대 개수
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
LINE = 100


def solve(N, line):
    DP = [[0 for _ in range(LINE)] for _ in range(LINE)]
    for r in range(LINE):
        for l in range(r, -1, -1):
            for k in range(l, r):
                DP[l][r] = max(DP[l][r], DP[l][k] + DP[k][r] + line[l][r])

    return DP[0][99]


def main():
    N = int(input())
    line = [[0 for _ in range(LINE)] for _ in range(LINE)]
    for _ in range(N):
        a, b = map(int, input().split())
        line[a-1][b-1] = 1
        line[b-1][a-1] = 1

    print(solve(N, line))


main()
