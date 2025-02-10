# 백준 31877

'''
각 작업들에 대해 우선순위 큐에 넣고 마감시간이 짧은 시간부터 꺼내 처리한다.
그 뒤 M개의 작업들이 추가되는 시간대까지만 작업을 하고 현재 작업을 우선순위 큐에 다시 넣는다.
우선순위 큐가 빌 때까지 위 작업을 반복하면 된다.
이미 쌓여있는 N개의 작업들은 시작 시간이 0으로 보면 된다.
'''

import io
import heapq

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# curTime 시간에 추가된 작업을 우선순위 큐 work에 추가
def addWork(curTime, work):
    for i in workDict[curTime]:
        heapq.heappush(work, i)

    return work


def solve():
    # 기존에 있던 작업 우선순위 큐에 추가
    work = addWork(0, [])
    curTime = 0
    timeIndex = 1

    # 모든 작업을 처리할 때까지 반복
    while True:
        # 우선순위 큐가 빌 때까지 반복
        while work:
            # 현재 해야 할 작업 체크
            curDeadline, curDuration, curStart = heapq.heappop(work)

            # 현재 작업을 끝냈을 때 마감시간이 지날 경우
            if curTime+curDuration > curDeadline:
                return ['NO']

            # 추가될 새 작업이 있는 경우
            if timeIndex < len(stopTime):
                # 현재 작업이 끝나는 시간 > 새 작업이 들어오는 시간
                if curTime + curDuration > stopTime[timeIndex]:
                    heapq.heappush(work, [curDeadline, curTime + curDuration - stopTime[timeIndex], curStart])
                    curTime = stopTime[timeIndex]
                    work = addWork(curTime, work)
                    timeIndex += 1
                # 현재 작업이 끝나는 시간 < 새 작업이 들어오는 시간
                elif curTime + curDuration < stopTime[timeIndex]:
                    curTime = curTime + curDuration
                # 현재 작업이 끝나는 시간 = 새 작업이 들어오는 시간
                else:
                    curTime = stopTime[timeIndex]
                    work = addWork(curTime, work)
                    timeIndex += 1
            # 추가될 새 작업이 없는 경우
            else:
                curTime = curTime + curDuration

        # 우선순위 큐가 비었고 아직 추가될 작업이 있는 경우
        if timeIndex < len(stopTime):
            curTime = stopTime[timeIndex]
            work = addWork(curTime, work)
            timeIndex += 1
        else:
            break

    return ['YES', curTime]


# main 함수 ----------
N = int(input())
workDict = dict()       # [마감 시각, 걸리는 시간, 작업이 추가되는 시각] 순으로 저장
for _ in range(N):
    t, d = map(int, input().split())
    if 0 not in workDict:
        workDict[0] = [[d, t, 0]]
    else:
        workDict[0].append([d, t, 0])

M = int(input())
stopTime = {0}
for _ in range(M):
    w, t, d = map(int, input().split())
    stopTime.add(w)
    if w not in workDict:
        workDict[w] = [[d, t, w]]
    else:
        workDict[w].append([d, t, w])
stopTime = sorted(list(stopTime))

for i in solve():
    print(i)
