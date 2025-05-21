# 백준 1102

'''
DP[status] = status 상태를 만들기 위해 필요한 최소 비용
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 1000


def solve(N, cost, start, P):
    MAX = (1<<N) - 1
    DP = [INF for _ in range(MAX+1)]

    # 켜져있는 발전소 비트마스킹 처리
    startStatus = 0
    for i in range(N):
        if start[i] == 'Y':
            startStatus = startStatus | (1<<i)
    DP[startStatus] = 0

    result = INF
    for curStatus in range(MAX+1):
        # 켜져있는 발전소가 P개 이상인지 체크
        onCount = 0
        for i in range(N):
            if curStatus & (1<<i) != 0:
                onCount += 1
        if onCount >= P:
            result = min(result, DP[curStatus])
            continue

        # 시작 발전소가 전부 켜진 상태가 아니라면
        if curStatus & startStatus != startStatus:
            continue

        # curStatus 상태에서 켜진 발전소가 꺼진 발전소를 켤 때 비용 갱신
        for onGen in range(N):
            if curStatus & (1<<onGen) == 0:
                continue

            for offGen in range(N):
                if curStatus & (1<<offGen) != 0:
                    continue

                nextStatus = curStatus | (1<<offGen)
                DP[nextStatus] = min(DP[nextStatus], DP[curStatus]+cost[onGen][offGen])

    if result == INF:
        return -1
    return result


def main():
    N = int(input())
    cost = []
    for _ in range(N):
        cost.append(list(map(int, input().split())))
    start = list(input().decode().strip())
    P = int(input())

    print(solve(N, cost, start, P))


main()
