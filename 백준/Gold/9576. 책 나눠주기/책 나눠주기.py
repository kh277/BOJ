# 백준 9576

'''
원하는 책 번호 구간을 작업의 [시작 시간, 마감 시간]로 볼 경우,
시작 시간, 마감 시간이 주어지고, 작업 수행 시간이 1인 작업들을 최대한 많이 처리하는 문제로 볼 수 있다.
'''

import io
import heapq

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, M, task):
    result = 0
    task.sort(key= lambda x: (x[0], x[1]))
    pq = []

    taskIndex = 0
    for curTime in range(1, N+1):

        # 시작할 수 있는 작업 우선순위 큐에 삽입
        while taskIndex < M:
            if task[taskIndex][0] <= curTime:
                heapq.heappush(pq, [task[taskIndex][1], task[taskIndex][0]])
                taskIndex += 1
            else:
                break

        # 작업 수행
        while pq:
            curD, curR = heapq.heappop(pq)

            # 이미 taskIndex 작업의 마감 시간이 지난 경우
            if curD < curTime:
                continue
            # taskIndex 작업을 수행할 수 있는 경우
            elif curR <= curTime <= curD:
                result += 1
                break
            # taskIndex 작업의 시작 시간이 남은 경우
            else:
                break

    return result


def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        task = []
        for _ in range(M):
            s, e = map(int, input().split())
            task.append((s, e))

        print(solve(N, M, task))


main()
