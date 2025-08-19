# 백준 4781

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
ARRAY_TYPE = 'I'


def solve(N, maxCost, candy):
    prevDP = array(ARRAY_TYPE, [0]) * (maxCost+1)

    # 사탕1에 대한 DP 처리
    for cost in range(candy[0][1], maxCost+1):
        prevDP[cost] = prevDP[cost-candy[0][1]] + candy[0][0]

    # 사탕2 이후에 대한 DP 처리
    curDP = prevDP[:]
    for i in range(1, N):
        curCal, curPrice = candy[i]
        for cost in range(curPrice, maxCost+1):
            curDP[cost] = max(curDP[cost], curDP[cost-curPrice] + curCal)

        prevDP = curDP

    return prevDP[maxCost]


def main():
    while True:
        N, M = map(float, input().split())
        N = int(N)
        M = int(round(M*100))
        if N == 0 and M == 0:
            break
        candy = []
        for _ in range(N):
            c, p = map(float, input().split())
            candy.append([int(c), int(round(p*100))])

        print(solve(N, M, candy))


main()
