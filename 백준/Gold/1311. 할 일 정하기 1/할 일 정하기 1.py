# 백준 1311

'''
번호 순서대로 일을 배정. 비트마스크에 1이 4개라면 1~4번 사람은 이미 일이 할당된 것임.
DP[i] = 현재 마스크(할당된 일 여부)가 i일 때, 필요한 비용의 최소값 
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**8


def solve(N, cost):
    DP = [INF for _ in range(1<<N)]
    DP[0] = 0
    for status in range(1<<N):
        cur = bin(status).count("1")

        # cur번째 사람에게 task번째 일을 시키기
        for task in range(N):
            if status & (1<<task) == 0:
                nextStatus = status | (1<<task)
                DP[nextStatus] = min(DP[nextStatus], DP[status]+cost[cur][task])

    return DP[(1<<N)-1]


def main():
    N = int(input())
    cost = []
    for _ in range(N):
        cost.append(list(map(int, input().split())))
    print(solve(N, cost))


main()
