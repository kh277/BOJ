# 백준 6115

'''
작업 시간 1, 마감 기한 D_i, 이익 P_i인 작업들을 스케줄링할 때,
얻는 최대의 이익을 구하는 문제이다.
작업의 마감 기한이 긴 작업부터 뒤에서 하나씩 처리하면서 최대의 이익을 갖도록 하면 된다.
'''

import io
import heapq

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**10


def solve(N, tasks):
    pq = []
    tasks.sort(key= lambda x: (-x[0], -x[1]))

    result = 0
    curT = INF
    index = 0
    while curT > 0 and (index < N or pq):

        # 큐에 추가할 작업이 없을 경우
        if not pq and tasks[index][0] < curT:
            curT = tasks[index][0]
            continue
        
        # 큐에 작업을 추가해야 하는 경우
        while index < N and tasks[index][0] >= curT:
            heapq.heappush(pq, -tasks[index][1])
            index += 1

        # 작업 수행
        result -= heapq.heappop(pq)
        curT -= 1

    return result


def main():
    N = int(input())
    tasks = []
    for _ in range(N):
        d, v = map(int, input().split())
        tasks.append([d, v])

    print(solve(N, tasks))


main()
