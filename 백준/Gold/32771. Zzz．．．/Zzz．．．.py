# 백준 32771

'''
스위핑을 통해 각 방마다 예약된 시간대를 저장한 뒤, 구간을 뒤집어 예약이 없는 시간대를 저장하자.
그 뒤, 모든 방에 대해 예약이 없는 시간대를 스위핑을 통해 합치면 정답이 된다.
'''

import sys

input = sys.stdin.readline
MAX_ROOM = 7


# 스위핑 : 예약 시간이 저장된 리스트 L을 스위핑으로 중복 제거 처리
def sweep(L):
    length = len(L)
    L.sort(key= lambda x: (x[0], x[1]))
    result = []
    start, end = L[0]

    for left, right in L[1:]:
        if end < left:
            result.append([start, end])
            start, end = left, right
        else:
            end = max(end, right)

    result.append([start, end])
    return result


# 구간 뒤집기 : 현재 방의 영업 시간(0 ~ limit)에 대해 예약이 없는 시간만 도출해 반환
def revSweep(L, limit):
    result = []
    start = 0
    for left, right in L:
        result.append([start, left])
        start = right

    if start < limit:
        result.append([start, limit])

    return result


def solve():
    interval = []
    # 스위핑으로 중복된 예약 시간 제거
    for i in range(MAX_ROOM):
        reserv[i] = sweep(reserv[i])
        interval.extend(revSweep(reserv[i], openHour[i]))
    
    # 스위핑으로 각 방마다 빈 시간을 합쳐 누적 시간 반환
    interval = sweep(interval)
    return sum(right - left for left, right in interval)


# main 함수 ----------
N = list(map(int, input().split()))
openHour = list(map(int, input().split()))
reserv = [[] for _ in range(MAX_ROOM)]

for i in range(MAX_ROOM):
    for j in range(N[i]):
        s, e = map(int, input().split())
        reserv[i].append([s, e])

print(solve())