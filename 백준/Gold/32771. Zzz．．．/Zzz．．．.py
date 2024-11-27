# 백준 32771

import sys

input = sys.stdin.readline
MAX_ROOM = 7


# 스위핑 : limit개의 예약 L을 스위핑으로 중복 제거 처리
def sweeping(L, limit):
    L.sort(key= lambda x: (x[0], x[1]))
    result = []
    start = L[0][0]
    end = L[0][1]
    index = 1

    while index < limit:
        if end < L[index][0]:
            result.append([start, end])
            start = L[index][0]
            end = L[index][1]
        else:
            end = max(end, L[index][1])
        index += 1
    
    if limit > 0:
        result.append([start, end])
    return result


def solve():
    index = [0 for _ in range(MAX_ROOM)]        # 현재까지 처리한 예약의 인덱스 저장
    time = sorted(list(timeSet))        # 예약된 시간대를 정렬해서 저장

    # curTime ~ nextTime동안 사용 가능한지 확인
    result = 0
    for i in range(1, len(time)):
        curTime = time[i-1]
        nextTime = time[i]
        addTime = 0

        # 모든 방에 대해 탐색
        for j in range(MAX_ROOM):
            # 모든 예약이 다 처리된 경우
            if index[j] == len(reserv[j]):
                if curTime >= openHour[j]:      # 영업 시간이 끝난 경우
                    continue
                else:       # 예약이 다 처리되었고, 영업 시간이 끝나지 않은 경우
                    addTime = nextTime - curTime
                    continue

            # nextTime에 예약이 끝나는 경우 -> index 증가
            elif nextTime == reserv[j][index[j]][1]:
                index[j] += 1
                continue

            # 잠방이 사용중인 경우
            elif curTime >= reserv[j][index[j]][0] and nextTime <= reserv[j][index[j]][1]:
                continue

            # 잠방이 빈 경우
            else:
                addTime = nextTime - curTime
                continue
        result += addTime

    return result


# main 함수 ----------
N = list(map(int, input().split()))
openHour = list(map(int, input().split()))
reserv = [[] for _ in range(MAX_ROOM)]
timeSet = set()     # 예약 시작 시간, 예약 끝 시간 및 방 마감 시간 전부 저장
timeSet.add(0)

for i in range(MAX_ROOM):
    for j in range(N[i]):
        s, e = map(int, input().split())
        reserv[i].append([s, e])
        timeSet.add(s)
        timeSet.add(e)
for i in openHour:
    timeSet.add(i)

# 스위핑으로 중복된 예약 시간 제거
for i in range(MAX_ROOM):
    reserv[i] = sweeping(reserv[i], N[i])

print(solve())