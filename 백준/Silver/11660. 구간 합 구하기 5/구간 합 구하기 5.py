# 백준 11660

'''
첫 번째 ~ k 번째까지 숫자의 누적 합을 DP 테이블에 저장한다.
이 작업을 모든 행에 대해 반복하면 된다.
'''

import sys

input = sys.stdin.readline


def cumul_sum(N: int, graph: list) -> list:
    temp = [[] for _ in range(N+1)]

    # 각 행의 0번 인덱스는 사용하지 않음.
    for i in range(N+1):
        temp[i].append(0)
    
    # 각 행의 1번 인덱스부터 N번 인덱스까지의 누적 합 계산
    for i in range(N+1):
        for j in range(1, N+1):
            temp[i].append(graph[i][j] + temp[i][j-1])

    return temp


def get_sum(start: list, end: list) -> int:
    result = 0

    # 범위 내의 행에 대해 구간 합 누적
    for i in range(start[0], end[0]+1):
        result += DP[i][end[1]] - DP[i][start[1]-1]
    
    return result


def main():
    global DP
    N, M = map(int, input().split())

    graph = []
    graph.append([0] * (N+1))
    for _ in range(N):
        graph.append([0] + list(map(int, input().split())))
    
    DP = cumul_sum(N, graph)
    
    qurry = []
    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        print(get_sum([x1, y1], [x2, y2]))


main()