# 백준 27041

'''
DP[i] = 소가 i칸에 도착하기 위해 도약해야 하는 횟수
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**5


def solve(goalX, maxLeap, B, cows):
    DP = [INF for _ in range(goalX+1)]
    DP[0] = 0

    for curX in range(0, goalX):
        if curX in cows:
            continue
        for leap in range(1, maxLeap+1):
            if curX+leap in cows:
                continue
            if curX+leap <= goalX:
                DP[curX+leap] = min(DP[curX+leap], DP[curX]+1)
    
    return DP[goalX]


def main():
    E, L, B = map(int, input().split())
    cows = set()
    for _ in range(B):
        cows.add(int(input()))
    print(solve(E, L, B, cows))


main()
