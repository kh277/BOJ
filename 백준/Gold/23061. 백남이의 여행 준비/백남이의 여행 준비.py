# 백준 23061

'''
DP[i] = 무게제한이 i일 때, 얻을 수 있는 최대 가치
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, M, bag, limit):
    maxL = max(limit)
    beforeDP = [-1 for _ in range(maxL+1)]
    beforeDP[0] = 0

    # DP 계산
    for i in range(1, N+1):
        curDP = [-1 for _ in range(maxL+1)]
        curDP[0] = 0
        curW, curV = bag[i-1]
        for j in range(1, maxL+1):
            if j-curW >= 0:
                curDP[j] = max(curDP[j-1], beforeDP[j-curW]+curV, beforeDP[j])
            else:
                curDP[j] = max(curDP[j-1], beforeDP[j])
        beforeDP = curDP

    # 최대 효율 찾기
    maxEffi = -1
    maxIndex = 0
    for i in range(M):
        curL = limit[i]
        curEffi = beforeDP[curL] / curL
        if curEffi > maxEffi:
            maxEffi = curEffi
            maxIndex = i+1

    return maxIndex


def main():
    N, M = map(int, input().split())
    bag = []
    for _ in range(N):
        W, V = map(int, input().split())
        bag.append([W, V])

    limit = []
    for _ in range(M):
        limit.append(int(input()))
    print(solve(N, M, bag, limit))


main()
