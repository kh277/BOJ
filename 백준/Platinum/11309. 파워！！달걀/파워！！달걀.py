# 백준 11309

'''
DP[i][j] = 계란을 i번 던질 때, j개의 계란으로 확인할 수 있는 최대 층 수
DP[i][j] >= N이 되는 최소 i를 찾기
'''

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
ARRAY_TYPE = 'I'
INF = 32


def getDP():
    DP = [array(ARRAY_TYPE, [0]) * (INF+1) for _ in range(INF+1)]

    # DP 계산
    for i in range(1, INF+1):
        for j in range(1, INF+1):
            if j == 1:
                DP[i][1] = i
            else:
                DP[i][j] = DP[i-1][j-1] + DP[i-1][j] + 1

    return DP


def query(N, K, DP):
    for i in range(INF+1):
        if DP[i][K] >= N:
            return i

    return 'Impossible'


def main():
    T = int(input())
    DP = getDP()
    for _ in range(T):
        N, K = map(int, input().split())
        print(query(N, K, DP))


main()
