# 백준 14464

'''
시작 시간, 끝 시간이 정해진 작업을 T_i에 처리할 때, 최대로 처리 가능한 작업 수 구하기.
-> 마감 시간이 빠른 것부터 처리하기
'''

import io
import heapq

input = io.BufferedReader(io.FileIO(0), 1<<18).readline

def solve(T, task):
    result = 0
    T.sort()
    task.sort(key= lambda x: (x[0], x[1]))
    pq = []

    taskIndex = 0
    for i in range(len(T)):
        curHelp = T[i]

        # 시작할 수 있는 작업 우선순위 큐에 삽입
        while taskIndex < len(task):
            if task[taskIndex][0] <= curHelp:
                heapq.heappush(pq, [task[taskIndex][1], task[taskIndex][0]])
                taskIndex += 1
            else:
                break

        # 작업 할당
        while pq:
            curD, curR = heapq.heappop(pq)

            # 이미 taskIndex 작업이 끝나버린 경우
            if curD < curHelp:
                continue
            # 닭이 taskIndex 작업을 도와줄 수 있는 경우
            elif curR <= curHelp <= curD:
                result += 1
                break
            # taskIndex 작업이 아직 시작하지 않은 경우
            else:
                break

    return result


def main():
    C, N = map(int, input().split())
    T = []
    for _ in range(C):
        T.append(int(input()))
    task = []
    for _ in range(N):
        task.append(list(map(int, input().split())))
    
    print(solve(T, task))


main()