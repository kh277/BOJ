# 백준 28015

'''
DP[i][j] = [0, i]번째 파이프 중 일부를 사용할 때의 길이가 j일 때, 획득 가능한 최대 용량
'''

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**7


def solve(N, L, data):
    befDP = array('i', [-1]) * (L+1)
    befDP[0] = INF

    for i in range(N):
        curDP = befDP[:]
        curL, curF = data[i]
        for length in range(L-curL+1):
            nextL = length+curL
            if befDP[length] != -1:
                if befDP[nextL] != -1:
                    curDP[nextL] = max(curDP[nextL], min(befDP[length], curF))
                else:
                    curDP[nextL] = min(befDP[length], curF)
        befDP = curDP

    return befDP[L]


def main():
    D, P = map(int, input().split())
    data = []
    for _ in range(P):
        data.append(list(map(int, input().split())))
    print(solve(P, D, data))


main()
