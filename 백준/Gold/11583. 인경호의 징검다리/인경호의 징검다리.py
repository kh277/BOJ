# 백준 11583

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**7


def solve(N, K, stone):
    # 2와 5의 인수 개수 저장
    two = [0 for _ in range(N)]
    five = [0 for _ in range(N)]
    for i in range(N):
        curS = stone[i]
        cur2 = 2
        while curS % cur2 == 0:
            two[i] += 1
            cur2 *= 2
        cur5 = 5
        while curS % cur5 == 0:
            five[i] += 1
            cur5 *= 5

    # 2를 최소로 포함시키도록 돌 밟기 
    DP2 = [INF for _ in range(N)]
    DP2[0] = two[0]
    for curX in range(N):
        for dx in range(1, K+1):
            nextX = curX + dx
            if 0 <= nextX < N:
                DP2[nextX] = min(DP2[nextX], DP2[curX]+two[nextX])
            else:
                break

    # 5를 최소로 포함시키도록 돌 밟기 
    DP5 = [INF for _ in range(N)]
    DP5[0] = five[0]
    for curX in range(N):
        for dx in range(1, K+1):
            nextX = curX + dx
            if 0 <= nextX < N:
                DP5[nextX] = min(DP5[nextX], DP5[curX]+five[nextX])
            else:
                break

    return min(DP2[N-1], DP5[N-1])


def main():
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        stone = list(map(int, input().split()))
        print(solve(N, K, stone))


main()
