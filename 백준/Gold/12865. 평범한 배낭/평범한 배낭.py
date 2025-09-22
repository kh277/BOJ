# 백준 12865

'''
DP[i][j] = [0, i]번째 물건까지 사용한 무게가 j일 때, 가치의 최대값
'''

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
ARRAY_TYPE = 'I'


def solve(N, K, bag):
    prevDP = array(ARRAY_TYPE, [0]) * (K+1)
    for i in range(1, N+1):
        curW, curV = bag[i-1]
        curDP = array(ARRAY_TYPE, [0]) * (K+1)
        for j in range(1, K+1):
            if j-curW >= 0:
                curDP[j] = max(curDP[j-1], prevDP[j-curW]+curV, prevDP[j])
            else:
                curDP[j] = max(curDP[j-1], prevDP[j])
        prevDP = curDP

    return prevDP[K]


def main():
    N, K = map(int, input().split())
    bag = []
    for _ in range(N):
        a, b = map(int, input().split())
        bag.append((a, b))

    print(solve(N, K, bag))


main()