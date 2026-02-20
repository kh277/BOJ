# 백준 2618

'''
DP[i][j] = 경찰차A가 마지막으로 처리한 사건이 i, 경찰차B가 마지막으로 처리한 사건이 j일 때, 이동한 최소 거리.
traceBack[i][j] = 각 경찰차가 마지막으로 처리한 사건이 i, j이며, 그때의 최소값을 만들었던 값의 변화량 저장.
양수라면 경찰차 A가 그 값만큼 이동한 것, 음수라면 경찰차 B가 그 값만큼 이동한 것.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 100000000


def solve(N, tasks):
    DP = [[INF] * (N+2) for i in range(N+2)]
    traceBack = [[-1] * (N+2) for i in range(N+2)]

    # 0번 사건과 1번 사건은 각 경찰차의 초기 위치 지정
    DP[0][1] = 0

    # DP 처리
    for i in range(1, N+1):
        for lastA in range(i):
            lastB = i
            if lastA == 1:
                continue
            # 경찰차A가 사건 i+1을 처리
            moveA = DP[lastA][lastB] + abs(tasks[lastA][0] - tasks[i+1][0]) + abs(tasks[lastA][1] - tasks[i+1][1])
            if DP[i+1][lastB] > moveA:
                DP[i+1][lastB] = moveA
                traceBack[i+1][lastB] = i+1 - lastA

            # 경찰차B가 사건 i+1을 처리
            moveB = DP[lastA][lastB] + abs(tasks[lastB][0] - tasks[i+1][0]) + abs(tasks[lastB][1] - tasks[i+1][1])
            if DP[lastA][i+1] > moveB:
                DP[lastA][i+1] = moveB
                traceBack[lastA][i+1] = lastB - (i+1)

        for lastB in range(1, i):
            lastA = i
            # 경찰차A가 사건 i+1을 처리
            moveA = DP[lastA][lastB] + abs(tasks[lastA][0] - tasks[i+1][0]) + abs(tasks[lastA][1] - tasks[i+1][1])
            if DP[i+1][lastB] > moveA:
                DP[i+1][lastB] = moveA
                traceBack[i+1][lastB] = i+1 - lastA

            # 경찰차B가 사건 i+1을 처리
            moveB = DP[lastA][lastB] + abs(tasks[lastB][0] - tasks[i+1][0]) + abs(tasks[lastB][1] - tasks[i+1][1])
            if DP[lastA][i+1] > moveB:
                DP[lastA][i+1] = moveB
                traceBack[lastA][i+1] = lastB - (i+1)

    # DP 테이블에서 최대값 도출
    minD = INF
    minA = 0
    minB = 0
    for i in range(N+1):
        if minD > DP[i][N+1]:
            minD = DP[i][N+1]
            minA = i
            minB = N+1
        if minD > DP[N+1][i]:
            minD = DP[N+1][i]
            minA = N+1
            minB = i

    # 최적해 역추적
    curA = minA
    curB = minB
    result = []
    while len(result) < N:
        prev = traceBack[curA][curB]
        result.append(1 if prev > 0 else 2)
        if prev > 0:
            curA -= prev
        else:
            curB += prev

    return [minD] + result[::-1]


def main():
    Y = int(input())
    N = int(input())
    tasks = [(1, 1), (Y, Y)]
    for _ in range(N):
        tasks.append(tuple(map(int, input().split())))

    for i in solve(N, tasks):
        print(i)


main()
