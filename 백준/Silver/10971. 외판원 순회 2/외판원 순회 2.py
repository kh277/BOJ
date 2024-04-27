# 백준 10971

'''
외판원 문제이지만, 2 <= N <= 10이므로 브루트포스로도 풀린다.
1. 방문하지 않은 next 도시들에 대해 here -> next -> start 로 돌아오는 비용을 계산한다.
2. 재귀를 통해 방문 도시를 늘려가며 반복한다.
3. 모든 도시를 방문할 때까지 1~2번을 반복한다.

주의 반례 :
4
0 1 0 0
0 0 1 0
0 0 0 1
1 0 0 0
'''

import sys

input = sys.stdin.readline


def TSP(graph: list, left: list, here: int) -> int:
    # 도시를 다 방문한 경우
    if len(left) == 0:
        if graph[here][0] == 0:
            return 10e8
        
        # 경로가 존재한다면 현재 지점에서 start 지점으로 복귀하면 됨
        return graph[here][0]
    
    result = 10e8

    # 방문하지 않은 도시들에 대해 반복
    for next in left:
        # here -> next -> start로 가는 비용 계산
        temp = graph[here][next] + TSP(graph, [x for x in left if x != next], next)

        # 갈 수 없다면 최대값 반환
        if graph[here][next] == 0:
            temp = 10e8

        # 최소값 갱신이 가능하다면 갱신
        if temp < result:
            result = temp
    
    return result


def main():
    N = int(input())
    graph = []

    for i in range(N):
        graph.append(list(map(int, input().split())))
    
    # 순회 문제이기 때문에 시작 지점은 어디를 잡든지 상관이 없음
    print(TSP(graph, [i for i in range(1, N)], 0))


main()
