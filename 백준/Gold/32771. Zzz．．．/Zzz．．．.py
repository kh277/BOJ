# 백준 32771

'''
스위핑을 통해 각 방마다 예약된 시간대를 저장한 뒤, 구간을 뒤집어 예약이 없는 시간대를 저장하자.
모든 방에 대해 예약이 없는 시간대를 스위핑을 통해 합치면 정답이 된다.
'''

import sys

input = sys.stdin.readline
MAX_ROOM = 7


# 스위핑 : limit개의 예약 L을 스위핑으로 중복 제거 처리
def sweep(L, limit):
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


# 구간 뒤집기 : 현재 방의 영업 시간(0 ~ limit)에 대해 예약이 없는 시간만 도출해 반환
def revSweep(L, limit):
    result = []
    start = 0
    for i in range(len(L)):
        result.append([start, L[i][0]])
        start = L[i][1]
    
    result.append([start, limit])
    return result


def solve():
    interval = []
    # 스위핑으로 중복된 예약 시간 제거
    for i in range(MAX_ROOM):
        reserv[i] = sweep(reserv[i], N[i])
        interval += revSweep(reserv[i], openHour[i])
    
    # 스위핑으로 각 방마다 빈 시간을 합쳐 누적 시간 반환
    result = 0
    for i in sweep(interval, len(interval)):
        result += i[1] - i[0]
    
    return result


# main 함수 ----------
N = list(map(int, input().split()))
openHour = list(map(int, input().split()))
reserv = [[] for _ in range(MAX_ROOM)]

for i in range(MAX_ROOM):
    for j in range(N[i]):
        s, e = map(int, input().split())
        reserv[i].append([s, e])

print(solve())