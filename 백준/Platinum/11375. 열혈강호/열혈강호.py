# 백준 11375

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def DFS(data: list, cur_worker: int, complete: list, assignA: list, assignB: list) -> bool:
    complete[cur_worker] = True

    # 현재 작업자가 할 수 있는 일에 대해 반복
    for work in data[cur_worker]:
        # 해당 일이 할당되지 않은 경우 할당
        if assignB[work] == 0:
            assignA[cur_worker] = work
            assignB[work] = cur_worker

            return True
            
        # 해당 일이 다른 작업자에게 할당되어 있지만, 그 작업자가 다른 일을 할 수 있는 경우
        elif not complete[assignB[work]] and DFS(data, assignB[work], complete, assignA, assignB):
            assignA[cur_worker] = work
            assignB[work] = cur_worker

            return True
        
    return False
    

def match(worker: int, work: int, data: list) -> int:
    # 각 작업에 할당된 작업자의 번호 저장 (-1은 미할당)
    # assignA[i]는 A그룹의 i번째 작업자와 매칭된 B그룹의 작업 번호 저장
    # assignB[i]는 B그룹의 i번째 작업 번호와 매칭된 A그룹의 작업자 저장
    assignA = [0 for _ in range(worker+1)]
    assignB = [0 for _ in range(work+1)]

    result = 0

    # 모든 작업자에 대해 반복
    for cur_worker in range(1, worker+1):
        # 아직 매칭되지 않은 경우
        if assignA[cur_worker] == 0:
            complete = [False for _ in range(worker+1)]

            # 현재 작업자에 대해 매칭 시도
            if DFS(data, cur_worker, complete, assignA, assignB):
                result += 1

    return result


def main():
    N, M = map(int, input().split())

    data = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        data[i] = list(map(int, input().split()))[1:]

    print(match(N, M, data))


main()
