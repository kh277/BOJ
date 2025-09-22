# 백준 14949

'''
현재 a마리의 미생물이 다음날 b마리의 미생물이 되는 경우의 수는 aHb이다.
또한, DP[day][i] = day날이 지나는 동안 미생물이 i마리 존재하는 경우의 수
라고 보면, DP[day][i] = sigma(DP[day-1][j] * (jHi), j = [1, i])가 된다.
'''

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
MOD = 1000000007
ARRAY_TYPE = 'I'


def solve(H, W):
    # 1H1 ~ wHw까지 값 계산
    tableH = [array(ARRAY_TYPE, [0]) * (W+1) for _ in range(W+1)]
    for i in range(1, W+1):
        tableH[1][i] = 1
        tableH[i][1] = i

    for i in range(2, W+1):
        for j in range(2, W+1):
            tableH[i][j] = (tableH[i-1][j] + tableH[i][j-1]) % MOD

    # DP 계산
    DP = [array(ARRAY_TYPE, [0]) * (W+1) for _ in range(H+1)]
    DP[0][1] = 1
    for day in range(1, H+1):
        for i in range(1, W+1):
            for j in range(1, W+1):
                DP[day][i] = (DP[day][i] + (DP[day-1][j] * tableH[j][i]) % MOD) % MOD

    return sum(DP[H]) % MOD


def main():
    H, W = map(int, input().split())
    print(solve(H, W))


main()
