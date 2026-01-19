# 백준 21342

import io
import heapq

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


class Event:
    def __init__(self, dx, dv, left, right):
        self.dx = dx
        self.dv = dv
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        a = self.dx * other.dv
        b = other.dx * self.dv
        if a != b:
            return a < b


def solve(N, drone):
    # 살아있는 드론 간 연결 리스트를 [생존 여부, 왼쪽 드론 번호, 오른쪽 드론 번호]로 생성
    isAlive = [[1, None, None]]
    for i in range(1, N):
        isAlive[i-1][2] = i
        isAlive.append([1, i-1, None])

    # 충돌 사건을 [충돌 시간(분자), 충돌 시간(분모), 왼쪽 충돌 드론 번호, 오른쪽 충돌 드론 번호]로 저장
    pq = []
    for i in range(1, N):
        left = drone[i-1]
        right = drone[i]
        if left[1] > right[1]:
            pq.append(Event(right[0]-left[0], left[1]-right[1], i-1, i))

    # 충돌 시간을 기준으로 pq 생성 및 충돌 처리
    heapq.heapify(pq)
    while pq:
        curEv = heapq.heappop(pq)
        curL = curEv.left
        curR = curEv.right

        # 두 드론이 전부 살아있는지 체크
        if isAlive[curL][0] & isAlive[curR][0] != 1:
            continue

        # 충돌 처리
        isAlive[curL][0] = 0
        isAlive[curR][0] = 0

        # 연결 리스트 수정
        curLL = isAlive[curL][1]
        curRR = isAlive[curR][2]
        while curLL != None:
            if isAlive[curLL][0] == 1:
                break
            curLL = isAlive[curLL][1]
        while curRR != None:
            if isAlive[curRR][0] == 1:
                break
            curRR = isAlive[curRR][2]
        if curLL != None:
            isAlive[curLL][2] = curRR
        if curRR != None:
            isAlive[curRR][1] = curLL

        # 충돌 사건 추가
        if curLL != None and curRR != None and drone[curLL][1] > drone[curRR][1]:
            heapq.heappush(pq, Event(drone[curRR][0]-drone[curLL][0], drone[curLL][1]-drone[curRR][1], curLL, curRR))

    # 남은 드론 체크
    count = 0
    leftI = []
    for i in range(N):
        if isAlive[i][0] == 1:
            leftI.append(i+1)
            count += 1

    return [[count], leftI]


def main():
    N = int(input())
    drone = []
    for _ in range(N):
        drone.append(tuple(map(int, input().decode().split())))
    
    for i in solve(N, drone):
        print(*i)


main()
